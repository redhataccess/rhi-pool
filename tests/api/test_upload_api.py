import logging
import unittest
import requests
from insights import archive_functions
from insights.config import Settings

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class UploadAPI(unittest.TestCase):
    def setUp(self):
        self.setting = Settings()
        self.session = requests.session()
        self.session.cert = self.setting.get_certs()
        self.session.verify = False
        self.base_url = self.setting.get('api', 'url')
        self.archive_location = self.setting.get('upload_archive', 'archive_file_path')

    def test_archive_upload(self):
        """ Testing api upload endpoint """
        self.system_id = archive_functions.get_system_id(self.archive_location)
        files = {'file': open(self.archive_location, "rb")}
        self.upload = self.session.post(self.base_url + '/v1/uploads/' + self.system_id,
                                        files=files)
        assert self.upload.status_code == 201
        logging.info("Upload done successfully")
