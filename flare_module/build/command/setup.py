import os
import re
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
    # engine dao-context.xml
    ENGINE_DAO = [
        FlarePath.ORACLE_HOME + '/webapps/engine/WEB-INF/dao-context.xml',
        FlarePath.FLARE_TEMP + '/webapps/engine/WEB-INF/dao-context.xml'
    ]
    # restapi dao-context.xml
    RESTAPI_DAO = [
        FlarePath.ORACLE_HOME + '/webapps/restapi/WEB-INF/dao-context.xml',
        FlarePath.FLARE_TEMP + '/webapps/restapi/WEB-INF/dao-context.xml'
    ]
    # search_engine
    SOLR_SETUP = [
        FlarePath.ORACLE_HOME + '/setup/search_engine/solr/app',
        FlareEnv.SOLR_URL['ORACLE']
    ]
    # add sql
    ADD_SQL_SETUP = [
        FlarePath.FLARE_FRAME + '/setup/oracle',
        FlarePath.ORACLE_HOME + '/setup/dbscript/common/ee_05_01_initData.sql',
        FlarePath.ORACLE_HOME + '/setup/dbscript/common/SVBOT/ee_05_02_sampleSceanrio_initData.sql'
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

    DBCP_DATA = [
        ['initialSize', 100],
        ['maxActive', 200],
        ['maxIdle', 200],
        ['minIdle', 50]
    ]


    def __init__(self):
        tempDir = ['/setup', '/conf']
        # create temp directory
        for dir in tempDir:
            path = FlarePath.FLARE_TEMP + dir
            if not os.path.exists(path):
                os.makedirs(path)


    def settings(self):
        self.set_properties()
        self.set_solr()
        self.add_sql()


    def set_properties(self):
        # - s: set value
        # - r: replace contents
        # - d: set dbcp
        self.modify_file('s', self.ENGINE_PROPERTIES[0], self.ENGINE_PROPERTIES[1])
        self.modify_file('s', self.SETUP_PROPERTIES[0], self.SETUP_PROPERTIES[1])
        self.modify_file('r', self.BUILD_FILE[0], self.BUILD_FILE[1])
        self.modify_file('d', self.ENGINE_DAO[0], self.ENGINE_DAO[1])
        self.modify_file('d', self.RESTAPI_DAO[0], self.RESTAPI_DAO[1])


    def modify_file(self, type, source, temp):
        sourceFile = open(source, 'r',  encoding='UTF8')
        tempFile = open(temp, 'w', encoding='UTF8')

        for line in sourceFile:
            if type == 's':
                line = self.set_value(line)
            elif type == 'r':
                line = self.replace_contents(line)
            elif type == 'd':
                line = self.set_dbcp(line)
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


    def set_dbcp(self, line):
        for dbcp in self.DBCP_DATA:
            property = dbcp[0]
            value = str(dbcp[1])
            if line.find(property) > -1:
                oldValue = re.findall('[0-9]+', line)
                line = line.replace(oldValue[0], value)

        return line


    def set_solr(self):
        solrPath = self.SOLR_SETUP[0] + '/solr.jar'
        if not os.path.isfile(solrPath):
            print('Download solr: {0}'.format(self.SOLR_SETUP[1]))
            wget.download(self.SOLR_SETUP[1], self.SOLR_SETUP[0])


    def add_sql(self):
        addFilePath = self.ADD_SQL_SETUP[0]
        initFilePath = self.ADD_SQL_SETUP[1]
        initSceanrioFilePath = self.ADD_SQL_SETUP[2]
        addFileList = os.listdir(addFilePath)

        for addFile in addFileList:
            sqlFilePath = addFilePath + '/' + addFile
            sqlFile = open(sqlFilePath, 'r', encoding='UTF8')
            initFile = open(initFilePath, 'a', encoding='UTF8')
            initSceanrioFile = open(initSceanrioFilePath, 'a', encoding='UTF8')

            for line in sqlFile:
                if addFile.find('INIT_DATA') > -1:
                    initFile.write('\n')
                    initFile.write(line)
                elif addFile.find('T_SCENARIO') > -1:
                    initSceanrioFile.write('\n')
                    initSceanrioFile.write(line)

            sqlFile.close()
            initFile.close()
            initSceanrioFile.close()

