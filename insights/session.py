import requests
from insights.config import Settings

class Session(Settings):
    """ Requests session config"""
    def __init__(self, verify=False):
        super(Session, self).__init__()
        self.session = requests.session()
        self.session.verify = verify
        self.session.cert = self.get_certs()

    def get_session(self):
        """"
        Return requests session
        :return:
        """
        return self.session
