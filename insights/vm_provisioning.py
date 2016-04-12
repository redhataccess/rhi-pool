""" Module for provisioning VMs on openstack for testing
"""
import novaclient
import time
from novaclient import client
import paramiko
import configparser
import sys
import subprocess


class VMError():
    """
    Raise errors for the Virtual machine

    """

class VirtualMachine():

    def get_openstack_client_instance(self):
        """
        Creates client object instance using openstack novaclient API
        :return: openstack client object

        """
        config=configparser.ConfigParser()
        config.read("pool.conf")
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
            return openstack_client

    def create_openstack_instance(self, instance_name, image_name, flavor_name, key_name, pool_name, timeout=5 ):
        self.os_client = self.get_openstack_client_instance()
        print self.os_client.servers.list()
        print self.os_client.networks.list()
        image = self.os_client.images.find(name=image_name)
        flavor = self.os_client.flavors.find(name=flavor_name)
        self.floating_ip = self.os_client.floating_ips.create(pool=pool_name)
        print 'Floating ip created: {0}'.format(self.floating_ip.ip)

        # Create openstack instance from given parameters
        print 'Creating openstack instance {0}'.format(instance_name)

        print self.os_client
        self.instance = self.os_client.servers.create(name=instance_name, flavor=flavor, image=image, key_name=key_name)
        # waiting for the instance to boot
        status = self.instance.status
        print "The VM is booting, status: {0}".format(status)
        while status == "BUILD":
            time.sleep(10)
            self.instance = self.os_client.servers.get(self.instance.id)
            print(".")
            status = self.instance.status

        print "The VM has been booted, status: {0}".format(status)

        # Assigning floating ip to instance
        print "Assigning floating ip to the instance"
        time_up = time.time() + int(timeout) * 60
        while True:
            if time.time() > time_up:
                print('The timeout for assigning the floating IP has reached!')
                sys.exit(1)
            try:
                print time.time()
                self.instance.add_floating_ip(self.floating_ip)
                print('SUCCESS!! The floating IP {0} has been assigned '
                      'to instance!'.format(self.floating_ip.ip))
                break
            except novaclient.exceptions.BadRequest:
                time.sleep(5)

        print self.os_client.servers.find(name=instance_name).addresses
        print "Trying to ping the instance"
        print self.instance.id
        self.ping(self.floating_ip.ip, instance_name)

    def ping(self, host_ip, instance_name, timeout=5):
        """
        being able to ping the hostname using the floating ip assigned to the machine
        :param host_ip:
        :param instance_name:
        :param timeout:
        :return:
        """
        timeup = time.time() + int(timeout) * 60
        while True:
            command = subprocess.Popen(
                'ping -c1 {0}; echo $?'.format(host_ip),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True
            )
            output = command.communicate()[0]
            print output

            # Checking if the ping to the openstack instance is successful
            if int(output.split()[-1]) == 0:
                print(
                    'SUCCESS !! The given host {0} has been pinged!!'.format(instance_name))
                break
            elif time.time() > timeup:
                print(
                    'The timeout for pinging the host {0} has reached!'.format(instance_name)
                )
                sys.exit(1)
            else:
                time.sleep(5)

    def delete_openstack_instance(self, instance_name):
        """
        deleting the openstack instance created above
        :param instance_name:
        :return:
        """
        self.os_client.floating_ips.delete(self.floating_ip)
        print 'deleting instance: {0}'.format(instance_name)
        print self.instance.id
        self.instance.delete()






