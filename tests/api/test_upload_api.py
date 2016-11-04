import logging
import unittest
import requests
from insights import archive_functions
from insights.config import Settings
from insights.session import Session
from insights.configs import log_settings
from insights.utils.util import Util

LOGGER = logging.getLogger('insights_api')


class UploadAPI(unittest.TestCase):
    def setUp(self):
        self.setting = Settings()
        log_settings.configure()
        session_instance = Session()
        self.session = session_instance.get_session()
        self.base_url = self.setting.get('api', 'url')
        self.archive_location = self.setting.get('upload_archive', 'archive_file_path')

    def setup_method(self, method):
        Util.print_testname(type(self).__name__, method)

    def test_archive_upload(self):
        """ Testing api upload endpoint """
        self.system_id = archive_functions.get_system_id(self.archive_location)
        files = {'file': open(self.archive_location, "rb")}
        self.upload = self.session.post(self.base_url + '/v1/uploads/' + self.system_id,
                                        files=files)
        assert self.upload.status_code == 201
        LOGGER.info("Upload done successfully")
