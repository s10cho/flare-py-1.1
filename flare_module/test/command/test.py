import os
from datetime import datetime
from fabric.api import *
from config import FlareEnv, FlareResult, FlarePath
from decorator import before, remote

@before(remote(FlareEnv.SERVER["GATLING"]))
class Test():

    MVN_TEST = 'mvn -Dtest=FlareParam -DsimulationClass={0} -DoutputDirectoryBaseName={1} {2} test'

    INIT_SIMULATION = FlareEnv.TEST['INIT']

    TALK_SIMULATION = FlareEnv.TEST['TALK']

    SCENARIO_TALK_SIMULATION = FlareEnv.TEST['SCENARIO_TALK']

    CHATBOT_TALK_SIMULATION = FlareEnv.TEST['CHATBOT']

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


    def init_data(self):
        self.simulation(self.INIT_SIMULATION)


    def talk_test(self):
        self.simulation(self.TALK_SIMULATION)


    def scenario_talk_test(self):
        self.simulation(self.SCENARIO_TALK_SIMULATION)


    def chatbot_talk_test(self):
        self.simulation(self.CHATBOT_TALK_SIMULATION)


    def simulation(self, simulationList):
        if len(simulationList) < 0:
            print('No Simulation')
            return

        with cd(FlareResult.REMOTE_GATLING_HOME):           # cd gatling home
            for simulation in simulationList:               # loop simulation run
                self.simulation_run(simulation)             # maven test
                self.result_download()                      # download gatling report


    def simulation_run(self, simulation):
        testId = simulation["TEST_ID"]
        jvm = " ".join(['-D' + jvm for jvm in simulation["JVM"]])
        simulationClass = simulation["SIMULATION_CLASS"]
        outputDirectoryBaseName = simulationClass[simulationClass.rfind('.') + 1:] + '_' + testId
        self.execute(self.MVN_TEST.format(simulationClass, outputDirectoryBaseName, jvm))


    def result_download(self):
        with cd(FlareResult.REMOTE_GATLING_RESULT):
            lsOutput = run('ls')
            fileNames = lsOutput.split()
            for fileName in fileNames:
                file = fileName.split('-')
                timestamp = file[1]
                timestamp = datetime.fromtimestamp(int(timestamp) / 1000).strftime('%Y%m%d%H%M%S')
                date = timestamp[:8]
                downloadPath = self.FLARE_RESILT_GATLING + '/' + date
                changeFilename = file[0] + '-' + timestamp

                run('tar -cf {0}.tar {0}'.format(fileName))             # tar gatling report
                local('mkdir -p {0}'.format(downloadPath))              # mkdir download path
                get('{0}.tar'.format(fileName), downloadPath)           # download gatling.tar
                run('rm -rf {0}*'.format(fileName))                     # remove gatling report

            with lcd(downloadPath):
                local('tar -xf {0}.tar'.format(fileName))               # tar gatling report
                local('rm -rf {0}.tar'.format(fileName))                # remove tar file
                local('mv {0} {1}'.format(fileName, changeFilename))    # change name





