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


class NoCertificateException(Exception):
    """
    No certificate exception
    Valid values are :
        certs
        sat6
    """


@singleton
class Session:
    """
    Requests session object
    """
    def __init__(self):
        self.session = None
        self.settings = Settings()

    def get_session(self, certs="certs", verify=None):
        """
        Returns requests sesssion object
        Returns if already created or creates new one
        :return:
        """
        if self.session is None:
            return self._create_session(certs, verify)
        else:
            return self.session

    def _get_certs(self):
        """Get certificate details for session creation"""
        return self.settings.get_certs()

    def _get_sat6_certs(self):
        """Get certificate details for session creation"""
        return self.settings.get_sat6_certs()

    def _create_session(self, certs, verify):
        """
        Function to set all values required for session
        :return:
        """
        self.session = requests.session()
        if certs == "certs":
            self.session.verify = verify
            self.session.cert = self._get_certs()
        elif certs == "sat6":
            self.session.cert = self._get_sat6_certs()
            self.session.verify = verify
        else:
            raise NoCertificateException
        return self.session
