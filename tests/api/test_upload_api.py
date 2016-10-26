import json
import logging
import os
import shutil
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
        self.search_file_path = self.setting.get('upload_archive', 'search_file_path')
        self.bash_version = self.setting.get('upload_archive', 'bash_version')
        self.new_bash_version = self.setting.get('upload_archive', 'new_bash_version')
        self.un_archive_file_location = self.setting.get('upload_archive', 'un_archive_file_location')
        self.archive_location = self.setting.get('upload_archive', 'archive_file_path')

    def test_archive_upload(self):
        """ Testing api upload endpoint """
        self.system_id = archive_functions.get_system_id(self.archive_location)
        files = {'file': open(self.archive_location, "rb")}
        self.upload = self.session.post(self.base_url + '/v1/uploads/' + self.system_id,
                                        files=files)
        assert self.upload.status_code == 201
        logging.info("Upload done successfully")

    def test_upload_new_archive(self):
        """ Uploading new modified archive and checking if rule is detected """
        self.system_id = archive_functions.get_system_id(self.archive_location)
        archive_functions.replace_bash_version(self.search_file_path,self.un_archive_file_location,self.bash_version,
                                               self.new_bash_version)
        new_archive_file = {'file': open('tarfile_add.tar.gz', "rb")}
        upload_archive = self.session.post(self.base_url + '/v1/uploads/' + self.system_id,
                                           files=new_archive_file)
        assert upload_archive.status_code == 201

        response = json.loads(upload_archive.text)
        test_rule = 'bash_injection|VULNERABLE_BASH_DETECTED'
        reports = response['reports']
        matching_reports = [report for report in reports if report['rule_id'] == test_rule]
        logging.info(matching_reports)
        assert len(matching_reports) == 1
        """Checking bash version"""
        bash_version = matching_reports[0]
        assert bash_version['details']['package'] == self.new_bash_version
        logging.info("archive uploaded successfully, bash vulnerability detected")

    def tearDown(self):
        """ Deleting archive """
        if os.path.exists('tarfile_add.tar.gz'):
            os.remove('tarfile_add.tar.gz')
        shutil.rmtree(self.un_archive_file_location)
        logging.info('successfully deleted tarfile')
