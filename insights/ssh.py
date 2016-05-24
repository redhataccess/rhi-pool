import paramiko
import logging
from insights.config import Settings
import time

logger = logging.getLogger(__name__)

class SSHConnection(Settings):

    def get_ssh_connection(self,ip):
        ssh_client = paramiko.SSHClient()
        logger.info("initiated paramiko client")
        ssh_client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        key_filename = self.get('ssh','key_path')

        while True:
            try:
                ssh_client.connect(hostname=ip, username="cloud-user",
                                        key_filename = key_filename)
                logger.debug("SSH connection established")
                break
            except paramiko.ssh_exception.NoValidConnectionsError:
                time.sleep(5)

        return ssh_client
