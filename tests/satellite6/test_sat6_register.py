import unittest
import logging
from insights import archive_functions
from insights.session import Session
from insights.utils.util import Util
from insights.utils.api_resources import system_api, system_api_v2, report_api, upload_api
from insights.decorators import skip_if_not_set
from insights.configs import settings

LOGGER = logging.getLogger('insights_sat6')


class Satellite6APITestCase(unittest.TestCase):

    @classmethod
    def setup_class(self):
        session_instance = Session()
        self.session = session_instance.get_session(certs="sat6",
                                                    verify=settings.sat62.sat6_cacert)

        self.base_url = settings.api.url
        self.remote_branch = settings.sat62.remote_branch
        self.remote_leaf = settings.sat62.remote_leaf
        self.system_id = settings.sat62.registered_machine_id
        self.hostname = settings.sat62.hostname
        self.archive_location = settings.upload_archive.archive_file_path
        LOGGER.info(self.hostname)
        LOGGER.info(self.system_id)

    def setup_method(self, method):
        Util.print_testname(type(self).__name__, method)

    @skip_if_not_set('sat62')
    def test_register_machine_sat6(self):
        """ Test if the system is registered with Satellite 6"""
        register = self.session.post(self.base_url + system_api_v2,
                                     json={'system_id': self.system_id,
                                           'hostname': self.hostname,
                                           'remote_branch': self.remote_branch,
                                           'remote_leaf': self.remote_leaf,
                                        })
        LOGGER.info(register.status_code)
        LOGGER.info(register.json())
        Util.log_assert(register.status_code == 200, "Machine register status code is not 200 OK")

    def test_registered_upload_archive(self):
        """Test the /upload api endpoint via Satellite 6"""
        self.system_id = archive_functions.get_system_id(self.archive_location)
        files = {'file': open(self.archive_location, "rb")}
        self.upload = self.session.post(self.base_url + upload_api + '/' +
                                        self.system_id, files=files)
        Util.log_assert(self.upload.status_code == 201, "Upload archive was not successful!")
        LOGGER.info("Upload done successfully")

    def test_unregister_machine_sat6(self):
        """ Test if the above registered system has been unregistered and not
         checking in.[sat 6]
         """
        unregister = self.session.delete(self.base_url + system_api + '/' +
                                         self.system_id)
        Util.log_assert(unregister.status_code == 204, "Unregister machine status code is not 204")
        check_if_unregistered = self.session.get(self.base_url + system_api + '/' +
                                                 self.system_id)
        response = check_if_unregistered.json()
        LOGGER.info(response)

        Util.log_assert(response['isCheckingIn'] == False,
                              "Incorrect value of isCheckingIn")

        Util.log_assert(response['unregistered_at'] is not None, "Unregistered at field is None")
        reports = self.session.get(self.base_url + report_api + '?system_id=' +
                                   self.system_id)
        LOGGER.info(reports.json())
        LOGGER.info(reports.status_code)


