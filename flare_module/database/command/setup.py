import os
from config import FlarePath, FlareEnv

class Setup():

    SETUP_FILE = FlarePath.ORACLE_HOME + '/setup/setup.properties'
    TEMP_SETUP_FILE = FlarePath.TEMP_HOME + '/setup/setup.properties'

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

    def setupInfoSet(self):
        setupFile = open(self.SETUP_FILE, 'r',  encoding='UTF8')
        tempFile = open(self.TEMP_SETUP_FILE, 'w', encoding='UTF8')
        for line in setupFile:
            newLine = self.changeSetInfo(line)
            tempFile.write(newLine)

        setupFile.close()
        tempFile.close()


    def changeSetInfo(self, line):
        data = line.split('=')
        if len(data) == 2:
            for setupData in self.ORACLE_SETUP_DATA:
                if data[0] == setupData[0]:
                    data[1] = setupData[1] + '\n'
                    line = '='.join(data)

        return line


