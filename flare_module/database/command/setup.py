import os
import shutil
import wget
from config import FlarePath, FlareEnv

class Setup():
    ENGINE_PROPERTIES = FlarePath.WORKSPACE_HOME + '/conf/engine.properties.oracle'
    TEMP_ENGINE_PROPERTIES = FlarePath.TEMP_HOME + '/conf/engine.properties.oracle'

    SETUP_FILE = FlarePath.ORACLE_HOME + '/setup/setup.properties'
    TEMP_SETUP_FILE = FlarePath.TEMP_HOME + '/setup/setup.properties'

    SOLR_SETUP_PATH = FlarePath.ORACLE_HOME + '/setup/search_engine/solr/app'
    SOLR_DOWNLOAD_URL = FlareEnv.SOLR_ORACLE_URL

    ORACLE_SETUP_DATA = [
        ['db.driverClassName',  FlareEnv.DB_ORACLE[0]],
        ['db.url',              FlareEnv.DB_ORACLE[1]],
        ['db.username',         FlareEnv.DB_ORACLE[2]],
        ['db.password',         FlareEnv.DB_ORACLE[3]],
        ['db.ownername',        FlareEnv.DB_ORACLE[4]],
        ['db.validationQuery',  FlareEnv.DB_ORACLE[5]],
    ]

    def __init__(self):
        tempSetupPath = FlarePath.TEMP_HOME + '/setup'
        if not os.path.exists(tempSetupPath):
            os.makedirs(tempSetupPath)
        pass

    def modyfySetup(self):
        self.modyfyFile(self.ENGINE_PROPERTIES, self.TEMP_ENGINE_PROPERTIES)
        self.modyfyFile(self.SETUP_FILE, self.TEMP_SETUP_FILE)

    def modyfyFile(self, source, temp):
        sourceFile = open(source, 'r',  encoding='UTF8')
        tempFile = open(temp, 'w', encoding='UTF8')
        for line in sourceFile:
            newLine = self.changeSetInfo(line)
            tempFile.write(newLine)

        sourceFile.close()
        tempFile.close()
        shutil.copy(temp, source)


    def changeSetInfo(self, line):
        data = line.split('=')
        if len(data) == 2:
            for setupData in self.ORACLE_SETUP_DATA:
                if data[0] == setupData[0]:
                    data[1] = setupData[1] + '\n'
                    line = '='.join(data)
        return line


    def setSolr(self):
        solrPath = self.SOLR_SETUP_PATH + '/solr.jar'
        if not os.path.isfile(solrPath):
            wget.download(self.SOLR_DOWNLOAD_URL, self.SOLR_SETUP_PATH)


