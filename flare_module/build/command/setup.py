import os
import shutil
import wget
from config import FlarePath, FlareEnv

class Setup():
    # engine.properties.oracle
    ENGINE_PROPERTIES = [
        FlarePath.PROJECT_EER_HOME + '/conf/engine.properties.oracle',
        FlarePath.FLARE_TEMP + '/conf/engine.properties.oracle'
    ]
    # setup.properties
    SETUP_PROPERTIES = [
        FlarePath.ORACLE_HOME + '/setup/setup.properties',
        FlarePath.FLARE_TEMP + '/setup/setup.properties'
    ]
    # build.xml
    BUILD_FILE = [
        FlarePath.ORACLE_HOME + '/setup/build.xml',
        FlarePath.FLARE_TEMP + '/setup/build.xml'
    ]
    # search_engine
    SOLR_SETUP = [
        FlarePath.ORACLE_HOME + '/setup/search_engine/solr/app',
        FlareEnv.SOLR_URL['ORACLE']
    ]
    # t_config_property
    CONFIG_PROPERTY_SETUP = [
        FlareEnv.OPTION['CONFIG_PROPERTY'],
        FlarePath.ORACLE_HOME + '/setup/dbscript/common/ee_05_01_initData.sql'
    ]

    SETUP_DATA = [
        ['db.driverClassName',  FlareEnv.DB['ORACLE']['DRIVER']],
        ['db.url',              FlareEnv.DB['ORACLE']['URL']],
        ['db.username',         FlareEnv.DB['ORACLE']['USERNAME']],
        ['db.password',         FlareEnv.DB['ORACLE']['PASSWORD']],
        ['db.ownername',        FlareEnv.DB['ORACLE']['OWNERNAME']],
        ['db.validationQuery',  FlareEnv.DB['ORACLE']['VALIDATION']],
        ['helper.useflag',      'Y'],
    ]

    def __init__(self):
        tempDir = [
            '/setup',
            '/conf'
        ]
        # create temp directory
        for dir in tempDir:
            path = FlarePath.FLARE_TEMP + dir
            if not os.path.exists(path):
                os.makedirs(path)

    def settings(self):
        self.set_properties()
        self.set_solr()
        self.add_config_update_sql()

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
            for setupData in self.SETUP_DATA:
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


    def add_config_update_sql(self):
        configList = self.CONFIG_PROPERTY_SETUP[0]

        for config in configList:
            propertyId = config[0]
            value = config[1]

            sql = [
                "\n",
                "UPDATE t_config_property",
                "SET value = '{0}'".format(value),
                "WHERE property_id = '{0}';".format(propertyId),
                "\n"
            ]

            file = open(self.CONFIG_PROPERTY_SETUP[1], 'a', encoding='UTF8')
            file.write(" ".join(sql))
            file.close()
