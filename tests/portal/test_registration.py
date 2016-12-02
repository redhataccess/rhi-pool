import logging
from insights.vm_provisioning import VirtualMachine
from fauxfactory import gen_string
from insights.test import UITestCase
from insights.ui.session import Session
from insights.ui.navigator import Navigator

LOGGER = logging.getLogger('insights_portal')


class ClientRegisterTestCase(UITestCase):

    def setUp(self):
        super(ClientRegisterTestCase, self).setUp()
        self.vm = VirtualMachine()
        self.vm_name = 'vm_{0}'.format(gen_string('alpha', 6))
        LOGGER.info("Creating openstack instance - RHEL-7.1-x86_64")
        self.vm.create_openstack_instance(instance_name=self.vm_name, image_name='RHEL-7.1-x86_64',
                                          flavor_name='Tiny', key_name='jenkins-key', pool_name='public')

    def test_rhi_register(self):
        """
        Test for RHEL machine registration to Insights and verifying it
        on portal
        """
        self.vm.rhsm_register(distro='rhel7')
        self.vm.register_to_insights()
        self.host_name = self.vm.hostname.rstrip('\n')
        with Session(self.browser):
            Navigator(self.browser).go_to_inventory()
            self.inventory.search_inventory(self.host_name)
            self.inventory.wait_for_inventory_hostname(self.host_name)
            host, sys_type = self.inventory.get_inventory_details()
            self.assertEqual(self.host_name, str(host).strip(' '))
            self.assertEqual("RHEL Server", str(sys_type).strip(' '))

    def tearDown(self):
        LOGGER.info("Unregistering VM from RHI")
        self.vm.unregister_from_rhi()
        LOGGER.info("Unregistering VM from RHSM")
        self.vm.unregister_from_RHSM()
        self.vm.delete_openstack_instance(self.vm_name)