import unittest
import json, requests
from insights.config import Settings
from fauxfactory import gen_string

class RulesTestCase(unittest.TestCase):

    @classmethod
    def setup_class(self):
        self.setting = Settings()
        self.session = requests.session()
        self.session.cert = self.setting.get_certs()
        self.session.verify = False
        print self.session.cert
        print "got certs"
        self.base_url = self.setting.get('api', 'url')
        self.system_id  = gen_string('alphanumeric', 10)
        self.hostname = 'hostname_{0}'.format(gen_string('alpha', 12))

    def test_register_machine(self):

        register = self.session.post(self.base_url + '/v1/systems',
                                     data = {'system_id':self.system_id,
                                             'hostname':self.hostname})
        assert register.status_code == 201
        print register.json()

