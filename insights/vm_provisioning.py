""" Module for provisioning VMs on openstack for testing
"""

import novaclient
import time
from novaclient import client
import paramiko
import configparser
import sys
import subprocess


class VMError(Exception):
    """
    Raise errors for the Virtual machine

    """

class VirtualMachine():

    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read("pool.conf")
        self.rhn_username = self.config.get('rhn_login', 'rhn_username')
        self.rhn_password = self.config.get('rhn_login', 'rhn_password')

    def get_openstack_client_instance(self):
        """
        Creates client object instance using openstack novaclient API
        :return: openstack client object

        """
        username = self.config.get('openstack_vms','username')
        api_key = self.config.get('openstack_vms', 'api_key')
        auth_url = self.config.get('openstack_vms', 'auth_url')
        project_id = self.config.get('openstack_vms', 'project_id')
        with client.Client(
            version=2, username=username,
            api_key=api_key, auth_url=auth_url, project_id=project_id
        ) as openstack_client:
            openstack_client.authenticate()
            return openstack_client

    def create_openstack_instance(self, instance_name, image_name, flavor_name,
                                  key_name, pool_name, timeout=5 ):
        self.os_client = self.get_openstack_client_instance()
        print "List of existing servers: {0}".format(self.os_client.servers.list())
        image = self.os_client.images.find(name=image_name)
        flavor = self.os_client.flavors.find(name=flavor_name)
        self.floating_ip = self.os_client.floating_ips.create(pool=pool_name)
        print 'Floating ip created: {0}'.format(self.floating_ip.ip)

        # Create openstack instance from given parameters
        print 'Creating openstack instance {0}'.format(instance_name)
        print self.os_client
        self.instance = self.os_client.servers.create(name=instance_name,
                                                      flavor=flavor, image=image,
                                                      key_name=key_name)
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
                self.instance.add_floating_ip(self.floating_ip)
                print('SUCCESS!! The floating IP {0} has been assigned '
                      'to instance!'.format(self.floating_ip.ip))
                break
            except novaclient.exceptions.BadRequest:
                time.sleep(5)

        print "Addresses alloted to VM: {0}".format(self.os_client.servers.find(name=instance_name).addresses)
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

            # Checking if we can ping openstack instance
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

    def rhsm_register(self):
        """
        Register VM to subscription manager
        :return:
        """
        ip = self.floating_ip.ip
        self.ssh_client = paramiko.SSHClient()
        print self.ssh_client
        self.ssh_client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        while True:
            try:
                self.ssh_client.connect(hostname=ip, username="cloud-user")
                print "SSH connection established"
                break
            except paramiko.ssh_exception.NoValidConnectionsError:
                time.sleep(5)

        stdin, stdout, stderr = self.ssh_client.exec_command("hostname")
        self.hostname = stdout.read()
        print 'hostname: {0}'.format(self.hostname)

        cmd = 'sudo subscription-manager register --username={0} --password={1}'.format(
            self.rhn_username, self.rhn_password)

        stdin, stdout, stderr = self.ssh_client.exec_command(cmd, get_pty=True)
        print stdout.channel.recv_exit_status()
        print stdout.read(), stderr.read()
        print "RHSM registration done"

        cmd = 'sudo subscription-manager attach --auto'
        stdin, stdout, stderr = self.ssh_client.exec_command(cmd, get_pty=True)
        print stdout.read()
        status = stdout.channel.recv_exit_status()
        if status == 0:
            print "Auto subscription attached"
        else:
            raise VMError("Unable to attach auto subscription")

    def register_to_insights(self):
        """
        Register client to Subscription Manager
        Register the client to Red Hat Insights service
        :return:
        """
        self.rhsm_register()
        stdin,stdout,stderr = self.ssh_client.exec_command("sudo yum install -y redhat-access-insights", get_pty=True)
        print stdout.read()
        if stdout.channel.recv_exit_status() != 0:
            raise VMError("Unable to install redhat-access-insights rpm")

        stdin,stdout,stderr = self.ssh_client.exec_command("rpm -qi redhat-access-insights")
        print stdout.read()

        stdin, stdout, stderr = self.ssh_client.exec_command("sudo redhat-access-insights --register", get_pty=True)
        print stdout.read()
        if stdout.channel.recv_exit_status() != 0:
            print stderr.read()
            raise VMError("Registration to RHI not successful")

        stdin, stdout, stderr =  self.ssh_client.exec_command("sudo redhat-access-insights", get_pty=True)
        print stdout.read()
        if stdout.channel.recv_exit_status() !=0:
            raise VMError("Upload not successful")

        stdin, stdout, stderr = self.ssh_client.exec_command("cat /etc/redhat-access-insights/machine-id")
        self.machine_id = stdout.read()
        print self.machine_id
        return self.machine_id

    def unregister_from_rhi(self):
        """
        Unregister machine from Red Hat Insights service
        :return:
        """
        stdin, stdout, stderr =  self.ssh_client.exec_command("sudo redhat-access-insights --unregister", get_pty=True)
        print stdout.read()
        print stdout.channel.recv_exit_status()
        if stdout.channel.recv_exit_status() !=0:
            raise VMError("Unable to unregister the VM from RHI service")

    def unregister_from_RHSM(self):
        """
        Unregister machine from Subscription manager
        :return:
        """
        stdin, stdout, stderr = self.ssh_client.exec_command("sudo subscription-manager unregister", get_pty=True)
        print stdout.read()
        print stdout.channel.recv_exit_status()
        if stdout.channel.recv_exit_status() != 0:
            raise VMError("Unable to subscription-manager unregister")

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
