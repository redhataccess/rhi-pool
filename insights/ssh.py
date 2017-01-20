import paramiko
import logging
from insights.configs import settings
import time

logger = logging.getLogger(__name__)

class SSHError(Exception):
    """
    Raise errors for commands over ssh
    """

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

    def run(self, cmd, *args, **kwargs):
        """
        method for running ssh commands on the machine
        :param cmd:
        :param args:
        :param kwargs:
        :return:
        """
        stdin, stdout, stderr = self.ssh_client.exec_command(cmd, get_pty=True)
        self.stdout = stdout.readlines()
        self.stderr = stderr.read()
        error_code = stdout.channel.recv_exit_status()
        logger.info("Error code: {0}".format(error_code))
        logger.info(self.stdout)
        if error_code == 1:
            logger.error("Error: {0}".format(self.stderr))
            raise SSHError("Error in running '$insights-cli *' command")
        return self.stdout

    def copy_files(self, file, remote_dir_path, remote_file_location):
        """
        method for copying files from Base machine to remote machine
        :param file: the file to be copied
        :param remote_file_location: name of the file in remote location
        :return:
        """
        sftp = self.ssh_client.open_sftp()
        logger.info("Established sftp connection for copying the archives")
        try:
            logger.info("Checking if the path exists for remote directory")
            sftp.stat(remote_dir_path)
        except IOError:
            cmd = 'mkdir {0}'.format(remote_dir_path)
            self.run(cmd)
            logger.info("Created directory: {0}".format(remote_dir_path))

        sftp.put(file, remote_file_location)
        sftp.close()

    def close(self):
        self.ssh_client.close()
        logger.info("SSH connection closed")




