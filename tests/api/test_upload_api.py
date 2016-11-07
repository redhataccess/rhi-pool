import json
import logging
import os
import shutil
import unittest
import requests
from insights import archive_functions
from insights.config import Settings
from insights.session import Session
from insights.configs import log_settings

LOGGER = logging.getLogger('insights_api')
from insights.utils.util import Util


class UploadAPI(unittest.TestCase):
    def setUp(self):
        self.setting = Settings()
        log_settings.configure()
        session_instance = Session()
        self.session = session_instance.get_session()
        self.base_url = self.setting.get('api', 'url')
        self.new_bash_version = self.setting.get('upload_archive', 'new_bash_version')
        self.un_archive_file_location = self.setting.get('upload_archive', 'un_archive_file_location')
        self.archive_location = self.setting.get('upload_archive', 'archive_file_path')

    def setup_method(self, method):
        Util.print_testname(type(self).__name__, method)

    def test_archive_upload(self):
        """ Testing api upload endpoint """
        self.system_id = archive_functions.get_system_id(self.archive_location)
        files = {'file': open(self.archive_location, "rb")}
        print self.system_id
        self.upload = self.session.post(self.base_url + '/v1/uploads/' + self.system_id,
                                        files=files)
        assert self.upload.status_code == 201
        LOGGER.info("Upload done successfully")

    def test_upload_new_archive(self):
        """ Uploading new modified archive and checking if rule is detected """
        self.system_id = archive_functions.get_system_id(self.archive_location)

        archive_functions.replace_bash_version(self.un_archive_file_location,
                                               self.new_bash_version, self.archive_location)
        new_archive_file = {'file': open('tarfile_add.tar.gz', "rb")}
        upload_archive = self.session.post(self.base_url + '/v1/uploads/' + self.system_id,
                                           files=new_archive_file)
        assert upload_archive.status_code == 201

        response = json.loads(upload_archive.text)
        test_rule = 'bash_injection|VULNERABLE_BASH_DETECTED'
        reports = response['reports']
        matching_reports = [report for report in reports if report['rule_id'] == test_rule]
        LOGGER.info(matching_reports)
        assert len(matching_reports) == 1
        """Checking bash version"""
        bash_version = matching_reports[0]
        assert bash_version['details']['package'] == self.new_bash_version
        LOGGER.info("archive uploaded successfully, bash vulnerability detected")

    def tearDown(self):
        """ Deleting archive """
        if os.path.exists('tarfile_add.tar.gz'):
            os.remove('tarfile_add.tar.gz')
        shutil.rmtree(self.un_archive_file_location)
        LOGGER.info('successfully deleted tarfile')
