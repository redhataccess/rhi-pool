from fauxfactory import gen_string
import unittest
import logging
from insights.vm_provisioning import VirtualMachine,VMError
from insights.subset_functions import *
from insights.config import Settings
from insights.session import Session
from insights.configs import log_settings
from insights.utils.util import Util

LOGGER = logging.getLogger('insights_api')


class SubsetAPITestCase(unittest.TestCase):

  @classmethod
  def setup_class(self):
    self.vm1 = VirtualMachine()
    self.vm2 = VirtualMachine()
    self.vm1_name = 'vm_{0}'.format(gen_string('alpha', 6))
    self.vm2_name = 'vm_{0}'.format(gen_string('alpha', 6))
    self.vm1.create_openstack_instance(instance_name=self.vm1_name,
                                 image_name='RHEL-7.1-x86_64',
                                 flavor_name='Tiny', key_name='jenkins-key',
                                 pool_name='public')
    self.vm2.create_openstack_instance(instance_name=self.vm2_name,
                                 image_name='RHEL-7.2-x86_64',
                                 flavor_name='Tiny', key_name='jenkins-key',
                                 pool_name='public')
    self.setting = Settings()
    log_settings.configure()
    session_instance = Session()
    self.session = session_instance.get_session()
    self.base_url = self.setting.get('api', 'url')

  def setup_method(self, method):
      Util.print_testname(type(self).__name__, method)

  def test_subset_api_v1(self):
    """ Test subset creation using v1 api
    """
    self.system_ids = []
    LOGGER.info(self.vm1)
    self.vm1.rhsm_register(distro='rhel7')
    self.vm1.register_to_insights()
    LOGGER.info(self.vm1.hostname)
    LOGGER.info(self.vm1.machine_id)

    self.system_ids.append(self.vm1.machine_id)

    self.vm2.rhsm_register(distro='rhel7')
    self.vm2.register_to_insights()
    LOGGER.info(self.vm2)
    LOGGER.info(self.vm2.hostname)
    LOGGER.info(self.vm2.machine_id)
    self.system_ids.append(self.vm2.machine_id)
    LOGGER.info(self.system_ids)

    #create branch id
    self.branch_id = 'branch_{0}'.format(gen_string('alpha',12))
    self.payload = create_subset_payload(self.branch_id, self.system_ids)
    LOGGER.info(self.payload)
    # creating subsets at /v1/subsets
    subset_create = self.session.post(self.base_url + '/v1/subsets',
                                      json = self.payload)
    LOGGER.info(subset_create.ok)
    if subset_create.ok == True:
        LOGGER.info("Subset created successfully")
    else:
        LOGGER.info(subset_create.status_code, subset_create.text)

    response = subset_create.json()
    LOGGER.info(response)
    assert response["hash"] is not None
    assert response["length"] == len(self.system_ids)

    #Creating get request for the system_ids from a subset hash
    LOGGER.info("get request")
    get_subset = self.session.get(self.base_url + '/subsets/' + response["hash"] + '/systems')
    LOGGER.info(get_subset.ok)
    LOGGER.info(get_subset.text)

    response = get_subset.json()
    for system in response:
        LOGGER.info(system)
        LOGGER.info(system["system_id"])
        self.assertIn(system["system_id"], self.system_ids)
    LOGGER.info("assertion for /v1/subsets done, checking for /subsets... ")

    # check subset creation without /v1
    self.branch_id = 'branch_{0}'.format(gen_string('alpha',12))
    self.payload = create_subset_payload(self.branch_id, self.system_ids)
    LOGGER.info(self.payload)
    subset_create = self.session.post(self.base_url + '/subsets',
                                      json = self.payload)
    LOGGER.info(subset_create.ok)
    if subset_create.ok == True:
        LOGGER.info("Subset created successfully for /subsets")
    else:
        LOGGER.info(subset_create.status_code, subset_create.text)

    response = subset_create.json()
    LOGGER.info(response)
    assert response["hash"] is not None
    assert response["length"] == len(self.system_ids)

    #Creating get request for the system_ids from a subset hash
    LOGGER.info("get request")
    get_subset = self.session.get(self.base_url + '/subsets/' + response["hash"] + '/systems')
    LOGGER.info(get_subset.ok)
    LOGGER.info(get_subset.text)

    response = get_subset.json()
    for system in response:
        LOGGER.info(system)
        LOGGER.info(system["system_id"])
        self.assertIn(system["system_id"], self.system_ids)

  @classmethod
  def teardown_class(self):
    self.vm1.unregister_from_rhi()
    self.vm1.unregister_from_RHSM()
    self.vm1.delete_openstack_instance(instance_name=self.vm1_name)

    self.vm2.unregister_from_rhi()
    self.vm2.unregister_from_RHSM()
    self.vm2.delete_openstack_instance(instance_name=self.vm2_name)
