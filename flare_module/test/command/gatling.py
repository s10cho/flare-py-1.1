import os
from datetime import datetime
from fabric.api import *
from fabric.contrib.files import exists
from config import FlareEnv, FlareResult, FlarePath
from decorator import before, remote

@before(remote(FlareEnv.SERVER["GATLING"]))
class GatlingServer():

    SVN_CHECKOUT = 'svn update'

    MVN_TEST = 'mvn -Dtest=FlareParam -DsimulationClass={0} -DoutputDirectoryBaseName={1} {2} test'

    def __init__(self):
        resultDir = ['/report', '/report/gatling']
        # create result directory
        for dir in resultDir:
            path = FlarePath.FLARE_RESULT + dir
            if not os.path.exists(path):
                os.makedirs(path)
        self.FLARE_RESULT_GATLING = FlarePath.FLARE_RESULT + resultDir[1]


    def svn_update(self):
        # cd remote home
        with cd(FlareResult.REMOTE_GATLING_HOME):
            # svn update
            self.execute(self.SVN_CHECKOUT)

    def execute(self, command):
        if type(command) == list:
            command = " ".join(command)
        with settings(warn_only=True):
            run(command)


    def test_run(self, simulationClass, outputBaseName, jvm):
        run('rm -rf {0}/*'.format(FlareResult.REMOTE_GATLING_RESULT))                   # remove old report

        with cd(FlareResult.REMOTE_GATLING_HOME):                                       # cd gatling home
            self.execute(self.MVN_TEST.format(simulationClass, outputBaseName, jvm))    # run gatling

    def remove_old_report(self):
        if not exists(FlareResult.REMOTE_GATLING_RESULT):
            return

        with cd(FlareResult.REMOTE_GATLING_RESULT):
            lsOutput = run('ls')
            fileNames = lsOutput.split()
            for fileName in fileNames:
                run('rm -rf {0}*'.format(fileName))

    def result_download(self, outputBaseName):
        with cd(FlareResult.REMOTE_GATLING_RESULT):
            lsOutput = run('ls')
            fileNames = lsOutput.split()
            for fileName in fileNames:
                file = fileName.split('-')
                timestamp = file[1]
                date = timestamp[:8]
                time = datetime.now().strftime('%H%M%S')
                downloadPath = self.FLARE_RESULT_GATLING + '/' + date
                changeFilename = outputBaseName + '-' + date + time

                run('tar -cf {0}.tar {0}'.format(fileName))                 # tar gatling report
                local('mkdir -p {0}'.format(downloadPath))                  # mkdir download path
                get('{0}.tar'.format(fileName), downloadPath)               # download gatling.tar
                run('rm -rf {0}*'.format(fileName))                         # remove gatling report

                with lcd(downloadPath):
                    local('tar -xf {0}.tar'.format(fileName))               # tar gatling report
                    local('rm -rf {0}.tar'.format(fileName))                # remove tar file
                    local('mv {0} {1}'.format(fileName, changeFilename))    # change name

                    last_log_info = FlarePath.FLARE_RESULT + '/last_log_info'
                    f = open(last_log_info, 'w', encoding='UTF8')
                    f.write(downloadPath + '/' + changeFilename)
                    f.close()






