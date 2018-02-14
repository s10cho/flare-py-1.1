import os
import datetime
from fabric.api import *
from config import FlareEnv, FlareResult, FlarePath
from decorator import before, remote

@before(remote(FlareEnv.SERVER["GATLING"]))
class Test():

    MVN_TEST = 'mvn -Dtest=FlareParam -DsimulationClass={0} -DoutputDirectoryBaseName={1} test'

    INIT_SIMULATION_CLASS = FlareEnv.TEST['INIT']

    TALK_SIMULATION_CLASS = FlareEnv.TEST['TALK']

    SCENARIO_TALK_SIMULATION_CLASS = FlareEnv.TEST['SCENARIO_TALK']

    CHATBOT_TALK_SIMULATION_CLASS = FlareEnv.TEST['CHATBOT']

    def __init__(self):
        resultDir = ['/gatling']
        # create result directory
        for dir in resultDir:
            path = FlarePath.FLARE_RESULT + dir
            if not os.path.exists(path):
                os.makedirs(path)
        self.FLARE_RESILT_GATLING = FlarePath.FLARE_RESULT + resultDir[0]


    def execute(self, command):
        if type(command) == list:
            command = " ".join(command)
        with settings(warn_only=True):
            run(command)


    def simulation(self, simulationClassList):
        if len(simulationClassList) < 0:
            print('No Simulation')
            return
        # cd gatling home
        with cd(FlareResult.REMOTE_GATLING_HOME):
            # maven test
            for simulationClass in simulationClassList:
                self.simulation_run(simulationClass)
                self.result_download(simulationClass)


    def simulation_run(self, simulationClass):
        outputDirectoryBaseName = simulationClass[simulationClass.rfind('.') + 1:]
        self.execute(self.MVN_TEST.format(simulationClass, outputDirectoryBaseName))


    def result_download(self, simulationClass):
        outputDirectoryBaseName = simulationClass[simulationClass.rfind('.') + 1:]
        tarName = '{0}.tar'.format(outputDirectoryBaseName)

        with cd(FlareResult.REMOTE_GATLING_RESULT):
            lsOutput = run('ls')
            fileNames = lsOutput.split()
            for fileName in fileNames:
                file = fileName.split('-')
                timestamp = file[1]
                timestamp = datetime.datetime.fromtimestamp(int(timestamp) / 1000).strftime('%Y%m%d%H%M%S')
                date = timestamp[:8]
                time = timestamp[8:]
                downloadPath = self.FLARE_RESILT_GATLING + '/' + date

                run('tar -cf {0}.tar {0}'.format(fileName))     # tar gatling report
                local('mkdir -p {0}'.format(downloadPath))      # mkdir download path
                get('{0}.tar'.format(fileName), downloadPath)   # download gatling.tar
                run('rm -rf {0}*'.format(fileName))             # remove gatling report

            with lcd(downloadPath):
                local('tar -xf {0}.tar'.format(fileName))        # tar gatling report
                local('rm -rf {0}.tar'.format(fileName))         # remove tar file




    def init_data(self):
        self.simulation(self.INIT_SIMULATION_CLASS)


    def talk_test(self):
        self.simulation(self.TALK_SIMULATION_CLASS)


    def scenario_talk_test(self):
        self.simulation(self.SCENARIO_TALK_SIMULATION_CLASS)


    def chatbot_talk_test(self):
        self.simulation(self.CHATBOT_TALK_SIMULATION_CLASS)



