import unittest
import logging
from insights import archive_functions
from insights.config import Settings
from fauxfactory import gen_string
from insights.session import Session
from insights.configs import log_settings
from insights.utils.util import Util

LOGGER = logging.getLogger('insights_sat6')

class Satellite6APITestCase(unittest.TestCase):

    @classmethod
    def setup_class(self):
        self.setting = Settings()
        log_settings.configure()
        session_instance = Session()
        self.session = session_instance.get_session(certs="sat6",
                                                    verify=self.setting.get('sat62','sat6_cacert'))
        self.base_url = self.setting.get('api', 'url')
        self.remote_branch = self.setting.get('sat62','remote_branch')
        self.remote_leaf = self.setting.get('sat62', 'remote_leaf')
        self.system_id = self.setting.get('sat62', 'registered_machine_id')
        self.hostname = self.setting.get('sat62','hostname')
        self.archive_location = self.setting.get('upload_archive', 'archive_file_path')
        LOGGER.info(self.hostname)
        LOGGER.info(self.system_id)

    def setup_method(self, method):
        Util.print_testname(type(self).__name__, method)

    def test_register_machine_sat6(self):
        """ Test if the system is registered with Satellite 6"""
        register = self.session.post(self.base_url + '/v2/systems',
                                     json = {'system_id':self.system_id,
                                             'hostname':self.hostname,
                                             'remote_branch':self.remote_branch,
                                             'remote_leaf':self.remote_leaf,
                                             })
        LOGGER.info(register.status_code)
        LOGGER.info(register.json())
        assert register.status_code == 200

    def test_registered_upload_archive(self):
        """Test the /upload api endpoint via Satellite 6"""
        self.system_id = archive_functions.get_system_id(self.archive_location)
        files = {'file': open(self.archive_location, "rb")}
        self.upload = self.session.post(self.base_url + '/v1/uploads/' +
                                        self.system_id, files=files)
        assert self.upload.status_code == 201
        LOGGER.info("Upload done successfully")

    def test_unregister_machine_sat6(self):
        """ Test if the above registered system has been unregistered and not
         checking in.[sat 6]
         """
        unregister = self.session.delete(self.base_url + '/v1/systems/' +
                                         self.system_id)
        assert unregister.status_code == 204
        check_if_unregistered = self.session.get(self.base_url + '/v1/systems/' +
                                                 self.system_id)
        response = check_if_unregistered.json()
        LOGGER.info(response)
        assert response['isCheckingIn'] == False
        assert response['unregistered_at'] is not None
        reports = self.session.get(self.base_url + '/v1/reports?system_id=' +
                                   self.system_id)
        LOGGER.info(reports.json())
        LOGGER.info(reports.status_code)

