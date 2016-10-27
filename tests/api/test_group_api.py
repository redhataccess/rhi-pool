import json
import logging
import unittest
import requests
from fauxfactory import gen_string
from insights.config import Settings
from insights.session import Session
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class GroupsAPI(unittest.TestCase):
    def setup_class(self):
        self.setting = Settings()
        ses_instance = Session()
        self.session = ses_instance.get_session()
        self.base_url = self.setting.get('api', 'url')

    def test_create_delete_groups(self):
        """ Create and delete group test
        """ 
        self.display_name = gen_string('alpha', 8)
        #  Create group
        self.create_group = self.session.post(self.base_url + '/v1/groups',
                                              data={'display_name': self.display_name})
        assert self.create_group.status_code == 201
        self.result = self.create_group.text
        response = json.loads(self.result)
        self.group_name = response['display_name']
        assert self.group_name == self.display_name
        logging.info("Group created successfully")

        # Request groups
        self.request_groups = self.session.get(self.base_url + '/v1/groups/')
        assert self.request_groups.status_code == 200
        request_groups = self.request_groups.json()
        logging.info(request_groups)

        # Request group
        self.group_id = response['id']
        self.request_group = self.session.get(self.base_url + '/v1/groups/' + str(self.group_id))
        group_name = self.request_group.json()
        logging.info(group_name)
        assert self.request_group.status_code == 200
        request_group_response = self.request_group.text
        response_id = json.loads(request_group_response)
        response_group_id = response_id['id']
        assert response_group_id == self.group_id


        # Delete group
        self.delete_group = self.session.delete(self.base_url + '/v1/groups/' + str(self.group_id))
        assert self.delete_group.status_code == 204
        after_deleting_group = self.session.get(self.base_url + '/v1/groups/' + str(self.group_id))
        assert after_deleting_group.status_code == 404
        logging.info("Group deleted successfully")
