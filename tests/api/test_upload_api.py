import logging
import unittest
from insights import archive_functions
from insights.session import Session
from insights.configs import settings
from insights.utils.util import Util
from insights.utils.api_resources import upload_api

LOGGER = logging.getLogger('insights_api')


class UploadAPI(unittest.TestCase):
    def setUp(self):
        session_instance = Session()
        self.session = session_instance.get_session()
        self.base_url = settings.api.url
        self.archive_location = settings.upload_archive.archive_file_path

    def setup_method(self, method):
        Util.print_testname(type(self).__name__, method)

    def test_archive_upload(self):
        """ Testing api upload endpoint """
        self.system_id = archive_functions.get_system_id(self.archive_location)
        files = {'file': open(self.archive_location, "rb")}
        self.upload = self.session.post(self.base_url + upload_api + '/' + self.system_id,
                                        files=files)
        assert self.upload.status_code == 201
        LOGGER.info("Upload done successfully")
