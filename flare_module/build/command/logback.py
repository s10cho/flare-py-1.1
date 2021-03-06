import os
import shutil
from config import FlarePath

class Logback():
    # logback.xml
    LOG_BACK = [
        FlarePath.ORACLE_HOME + '/conf',
        FlarePath.FLARE_TEMP + '/conf'
    ]

    LOG_LEVEL_SET = [
        [
            'com.ibatis.sqlmap.engine.impl.SqlMapExecutorDelegateTimeOver', 'DEBUG'
        ]
    ]

    def __init__(self):
        tempDir = ['/conf']
        # create temp directory
        for dir in tempDir:
            path = FlarePath.FLARE_TEMP + dir
            if not os.path.exists(path):
                os.makedirs(path)

    def change_log_level(self):
        logbackList = self.logback_list()

        for logback in logbackList:
            source = os.path.join(self.LOG_BACK[0], logback)
            temp = os.path.join(self.LOG_BACK[1], logback)
            self.modify_file(source, temp)


    def logback_list(self):
        fileList = os.listdir(self.LOG_BACK[0])
        logbackList = []
        for file in fileList:
            if file[:7] == 'logback':
                logbackList.append(file)

        return logbackList


    def modify_file(self, source, temp):
        sourceFile = open(source, 'r',  encoding='UTF8')
        tempFile = open(temp, 'w', encoding='UTF8')

        for line in sourceFile:
            line = self.replace_contents(line)
            tempFile.write(line)

        sourceFile.close()
        tempFile.close()
        shutil.copy(temp, source)


    def replace_contents(self, line):
        # default
        line = line.replace('level=\"DEBUG\"', 'level=\"ERROR\"')
        line = line.replace('level=\"INFO\"', 'level=\"ERROR\"')

        # set
        for logger in self.LOG_LEVEL_SET:
            loggerName = logger[0]
            loggerLevel = logger[1]

            if line.find(loggerName) > -1:
                line = line.replace('level=\"ERROR\"', 'level=\"{0}\"'.format(loggerLevel))

        return line
