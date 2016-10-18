import unittest
from fauxfactory import gen_string
from insights.config import Settings
from insights.ui.login import LoginUI
from insights.ui.search import UISearch
from insights.vm_provisioning import VirtualMachine
from selenium import webdriver


class ClientRegisterTestCase(unittest.TestCase):
    def setUp(self):
        self.setting = Settings()
        self.chrome_driver = self.setting.get('rhn_login', 'chrome_driver_path')
        self.vm = VirtualMachine()
        self.vm_name = 'vm_{0}'.format(gen_string('alpha', 6))
        self.vm.create_openstack_instance(instance_name=self.vm_name, image_name='RHEL-7.1-x86_64',
                                          flavor_name='Tiny', key_name='jenkins-key', pool_name='public')
        self.driver = webdriver.Chrome(self.chrome_driver)
        self.login = LoginUI(self.driver)
        self.driver.get(self.login.base_url)

    def test_rhi_register(self):
        self.vm.rhsm_register(distro='rhel7')
        self.vm.register_to_insights()
        self.host_name = self.vm.hostname.rstrip('\n')
        # UI tests for checking registered system appeared on customer portal UI
        try:
            self.login.login_to_portal()
            self.search = UISearch(self.driver)
            self.result_text = self.search.register_system(self.host_name)
            self.assertIn(self.host_name, self.result_text)
        except Exception as err:
            self.search.take_screenshot()
            raise err

    def tearDown(self):
        self.vm.unregister_from_rhi()
        self.vm.unregister_from_RHSM()
        self.vm.delete_openstack_instance(self.vm_name)
        self.login.teardown()
