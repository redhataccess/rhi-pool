import requests
from insights.config import Settings


def singleton(cls):
    """
    Returns same instance if already created
    :param cls:
    :return:
    """
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance


@singleton
class Session:
    """
    Requests session object
    """
    def __init__(self, verify=False):
        self.session = None
        self.verify = verify
        self._create_session()

    def get_session(self):
        """
        Returns requests sesssion object
        Returns if already created or creates new one
        :return:
        """
        if self.session is None:
            return self._create_session()
        else:
            return self.session

    def _get_certs(self):
        """Get certificate details for session creation"""
        self.settings = Settings()
        return self.settings.get_certs()

    def _create_session(self):
        """
        Function to set all values required for session
        :return:
        """
        self.session = requests.session()
        self.session.verify = self.verify
        self.session.cert = self._get_certs()
        return self.session