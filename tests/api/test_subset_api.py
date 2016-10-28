from fauxfactory import gen_string
import unittest
from insights.vm_provisioning import VirtualMachine,VMError
from insights.subset_functions import *
import json
import requests
from insights.config import Settings
from insights.session import Session

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
    session_instance = Session()
    self.session = session_instance.get_session()
    self.base_url = self.setting.get('api', 'url')

  def test_subset_api_v1(self):
    """ Test subset creation using v1 api
    """
    self.system_ids = []
    print self.vm1
    self.vm1.rhsm_register(distro='rhel7')
    self.vm1.register_to_insights()
    print self.vm1.hostname
    print self.vm1.machine_id

    self.system_ids.append(self.vm1.machine_id)

    self.vm2.rhsm_register(distro='rhel7')
    self.vm2.register_to_insights()
    print self.vm2
    print self.vm2.hostname
    print self.vm2.machine_id
    self.system_ids.append(self.vm2.machine_id)
    print self.system_ids

    #create branch id
    self.branch_id = 'branch_{0}'.format(gen_string('alpha',12))
    self.payload = create_subset_payload(self.branch_id, self.system_ids)
    print self.payload
    # creating subsets at /v1/subsets
    subset_create = self.session.post(self.base_url + '/v1/subsets',
                                      json = self.payload)
    print subset_create.ok
    if subset_create.ok == True:
        print "Subset created successfully"
    else:
        print subset_create.status_code, subset_create.text

    response = subset_create.json()
    print response
    assert response["hash"] is not None
    assert response["length"] == len(self.system_ids)

    #Creating get request for the system_ids from a subset hash
    print "get request"
    get_subset = self.session.get(self.base_url + '/subsets/' + response["hash"] + '/systems')
    print get_subset.ok
    print get_subset.text

    response = get_subset.json()
    for system in response:
        print system
        print system["system_id"]
        self.assertIn(system["system_id"], self.system_ids)
    print "assertion for /v1/subsets done, checking for /subsets... "

    # check subset creation without /v1
    self.branch_id = 'branch_{0}'.format(gen_string('alpha',12))
    self.payload = create_subset_payload(self.branch_id, self.system_ids)
    print self.payload
    subset_create = self.session.post(self.base_url + '/subsets',
                                      json = self.payload)
    print subset_create.ok
    if subset_create.ok == True:
        print "Subset created successfully for /subsets"
    else:
        print subset_create.status_code, subset_create.text

    response = subset_create.json()
    print response
    assert response["hash"] is not None
    assert response["length"] == len(self.system_ids)

    #Creating get request for the system_ids from a subset hash
    print "get request"
    get_subset = self.session.get(self.base_url + '/subsets/' + response["hash"] + '/systems')
    print get_subset.ok
    print get_subset.text

    response = get_subset.json()
    for system in response:
        print system
        print system["system_id"]
        self.assertIn(system["system_id"], self.system_ids)

  @classmethod
  def teardown_class(self):
    self.vm1.unregister_from_rhi()
    self.vm1.unregister_from_RHSM()
    self.vm1.delete_openstack_instance(instance_name=self.vm1_name)

    self.vm2.unregister_from_rhi()
    self.vm2.unregister_from_RHSM()
    self.vm2.delete_openstack_instance(instance_name=self.vm2_name)
