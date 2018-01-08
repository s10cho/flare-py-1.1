import configparser

class Config(object):
    config = configparser.ConfigParser()
    config.read('conf/config.properties')

    def get(self, type, key):
        return self.config.get(type, key)