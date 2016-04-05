""" Module for provisioning VMs on openstack for testing
"""

import novaclient
import time
from novaclient import client
import paramiko
import configparser


class VMError():
    """
    Raise errors for the Virtual machine

    """

class VirtualMachine():

    def openstack_client(self):
        """
        Creates client object instance using openstack novaclient API
        :return: openstack client object

        """
        config=configparser.ConfigParser()
        config.read("pool.conf")
        print config.sections()
        username = config.get('openstack_vms','username')
        api_key = config.get('openstack_vms', 'api_key')
        auth_url=config.get('openstack_vms', 'auth_url')
        project_id=config.get('openstack_vms', 'project_id')
        with client.Client(
            version=2, username=username,
            api_key=api_key, auth_url=auth_url, project_id=project_id
        ) as openstack_client:
            openstack_client.authenticate()
        print openstack_client
        print dir(openstack_client)
        print openstack_client.type
        return openstack_client
