import paramiko
import logging
from insights.configs import settings
import time

logger = logging.getLogger(__name__)


class SSHConnection:
    def __init__(self):
        self.ssh_client = paramiko.SSHClient()
        logger.info("initiated paramiko client")
        self.ssh_client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        self.key_filename = settings.ssh.ssh_key_path

    def get_ssh_connection(self,ip):
        """
        get ssh_client instance for VMs created on openstack,
        specific user: cloud-user
        :param ip:
        :return: ssh_client
        """

        while True:
            try:
                self.ssh_client.connect(hostname=ip, username="cloud-user",
                                        key_filename=self.key_filename)
                logger.debug("SSH connection established")
                break
            except paramiko.ssh_exception.NoValidConnectionsError:
                time.sleep(5)

        return self.ssh_client

    def get_ssh_instance(self, hostname, username):
        """
        get an ssh instance for any VM, used for insights-cli VM.
        :param: hostname, username
        :return: ssh_client
        """
        while True:
            try:
                self.ssh_client.connect(hostname=hostname, username=username,
                                        key_filename=self.key_filename)
                logger.info("SSH connection established with %s", hostname)
                break
            except paramiko.ssh_exception.NoValidConnectionsError:
                time.sleep(5)
        return self.ssh_client



