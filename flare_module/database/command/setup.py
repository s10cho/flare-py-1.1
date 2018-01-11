import os
from config import FlarePath

class Setup():

    TEMPLATE_JDBC_ORACLE = 'engine.properties.oracle'
    TEMPLATE_JDBC_POSTGRESQL = 'engine.properties.postgresql'
    SETUP_FILE = FlarePath.ORACLE_HOME + '/setup/setup.properties'
    TEMP_SETUP_FILE = FlarePath.TEMP_HOME + '/setup/setup.properties'

    def __init__(self):
        tempSetupPath = FlarePath.TEMP_HOME + '/setup'
        if not os.path.exists(tempSetupPath):
            os.makedirs(tempSetupPath)
        pass

    def jdbcInfoSet(self):
        pass

    def setupInfoSet(self):

        with open(self.SETUP_FILE, 'r', encoding='UTF8') as setupFile:
            with open(self.SETUP_FILE, 'w', encoding='UTF8') as tempFile:
                for line in setupFile:
                    tempFile.write(line)

    def get_template(self, template_name):
        template_path = 'template/' + template_name
        with open(template_path, 'r', encoding='UTF8') as f:
            template = f.read()

        return template


