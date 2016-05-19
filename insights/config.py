import configparser


class Settings(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('pool.conf')

    def get(self, section, option):
        return self.config.get(section, option)
