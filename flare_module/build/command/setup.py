import os
import shutil
import wget
from config import FlarePath, FlareEnv

class Setup():
    # engine.properties.oracle
    ENGINE_PROPERTIES = [
        FlarePath.WORKSPACE_HOME + '/conf/engine.properties.oracle',
        FlarePath.TEMP_HOME + '/conf/engine.properties.oracle'
    ]
    # setup.properties
    SETUP_PROPERTIES = [
        FlarePath.ORACLE_HOME + '/setup/setup.properties',
        FlarePath.TEMP_HOME + '/setup/setup.properties'
    ]
    # build.xml
    BUILD_FILE = [
        FlarePath.ORACLE_HOME + '/setup/build.xml',
        FlarePath.TEMP_HOME + '/setup/build.xml'
    ]
    # search_engine
    SOLR_SETUP = [
        FlarePath.ORACLE_HOME + '/setup/search_engine/solr/app',
        FlareEnv.SOLR_URL['ORACLE']
    ]

    ORACLE_SETUP_DATA = [
        ['db.driverClassName',  FlareEnv.DB['ORACLE']['DRIVER']],
        ['db.url',              FlareEnv.DB['ORACLE']['URL']],
        ['db.username',         FlareEnv.DB['ORACLE']['USERNAME']],
        ['db.password',         FlareEnv.DB['ORACLE']['PASSWORD']],
        ['db.ownername',        FlareEnv.DB['ORACLE']['OWNERNAME']],
        ['db.validationQuery',  FlareEnv.DB['ORACLE']['VALIDATION']],
    ]

    def __init__(self):
        tempDir = [
            '/setup',
            '/conf'
        ]
        # create temp directory
        for dir in tempDir:
            path = FlarePath.TEMP_HOME + dir
            if not os.path.exists(path):
                os.makedirs(path)

    def settings(self):
        self.set_properties()
        self.set_solr()

    def set_properties(self):
        # - s: set value
        # - r: replace contents
        self.modify_file('s', self.ENGINE_PROPERTIES[0], self.ENGINE_PROPERTIES[1])
        self.modify_file('s', self.SETUP_PROPERTIES[0], self.SETUP_PROPERTIES[1])
        self.modify_file('r', self.BUILD_FILE[0], self.BUILD_FILE[1])

    def modify_file(self, type, source, temp):
        sourceFile = open(source, 'r',  encoding='UTF8')
        tempFile = open(temp, 'w', encoding='UTF8')

        for line in sourceFile:
            if type == 's':
                line = self.set_value(line)
            elif type == 'r':
                line = self.replace_contents(line)
            tempFile.write(line)

        sourceFile.close()
        tempFile.close()
        shutil.copy(temp, source)

    def set_value(self, line):
        data = line.split('=')
        if len(data) == 2:
            for setupData in self.ORACLE_SETUP_DATA:
                if data[0] == setupData[0]:
                    data[1] = setupData[1] + '\n'
                    line = '='.join(data)
        return line

    def replace_contents(self, line):
        line = line.replace('<input', '<!--input')
        line = line.replace('</input>', '</input-->')

        return line

    def set_solr(self):
        solrPath = self.SOLR_SETUP[0] + '/solr.jar'
        if not os.path.isfile(solrPath):
            print('Download solr: {0}'.format(self.SOLR_SETUP[1]))
            wget.download(self.SOLR_SETUP[1], self.SOLR_SETUP[0])
