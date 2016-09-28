import configparser


class Settings(object):
    def __init__(self):
        super(Settings, self).__init__()
        self.config = configparser.ConfigParser()
        self.config.read('pool.conf')

    def get(self, section, option):
        return self.config.get(section, option)

    def get_certs(self):
        cert = self.get('certs', 'cert_path')
        key = self.get('certs', 'key_path')
        return cert, key

    def get_sat6_certs(self):
        sat6_cert = self.get('sat62', 'sat6_cert')
        sat6_key = self.get('sat62', 'sat6_key')
        return sat6_cert, sat6_key

