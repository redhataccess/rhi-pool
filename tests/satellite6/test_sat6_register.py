import unittest
import json, requests
from insights.config import Settings
from fauxfactory import gen_string
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class Satellite6APITestCase(unittest.TestCase):

    @classmethod
    def setup_class(self):
        self.setting = Settings()
        self.session = requests.session()
        self.session.cert = self.setting.get_sat6_certs()
        self.session.verify = self.setting.get('sat62','sat6_cacert')
        self.base_url = self.setting.get('api', 'url')
        self.remote_branch = self.setting.get('sat62','remote_branch')
        self.remote_leaf = self.setting.get('sat62', 'remote_leaf')
        self.system_id = self.setting.get('sat62', 'registered_machine_id')
        self.hostname = self.setting.get('sat62','hostname')
        print 'Hostname: {0}, System_id: {1}'.format(self.hostname,
                                                           self.system_id)
    def test_register_machine(self):
        # Test if the system is registered
        register = self.session.post(self.base_url + '/v2/systems',
                                     json = {'system_id':self.system_id,
                                             'hostname':self.hostname,
                                             'remote_branch':self.remote_branch,
                                             'remote_leaf':self.remote_leaf,
                                             })
        print register.status_code
        logging.info(register.json())
        assert register.status_code == 200

    def test_unregister_machine(self):
        # Test if the above registered system has been unregistered and not
        # checking in.
        unregister = self.session.delete(self.base_url + '/v1/systems/' +
                                         self.system_id)
        assert unregister.status_code == 204
#        check_if_unregistered = self.session.get(self.base_url + '/v1/systems/' +
#                                          self.system_id)
#        response = check_if_unregistered.json()
#        logging.info(response)
#        assert response['isCheckingIn'] == False
#        assert response['unregistered_at'] is not None
#        reports = self.session.get(self.base_url + '/v1/reports?system_id=' +
#                                          self.system_id)
#        print reports.json()
#        print reports.status_code
