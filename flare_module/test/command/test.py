import os
import wget
from fabric.api import *
from config import FlareEnv, FlareDeploy, FlarePath
from decorator import before, remote

@before(remote(FlareEnv.SERVER["GATLING"]))
class Test():

    MVN_TEST = 'mvn -Dtest=FlareParam -DsimulationClass={0} test'

    INIT_SIMULATION_CLASS = FlareEnv.TEST['INIT']

    TALK_SIMULATION_CLASS = FlareEnv.TEST['TALK']

    SCENARIO_TALK_SIMULATION_CLASS = FlareEnv.TEST['SCENARIO_TALK']

    CHATBOT_TALK_SIMULATION_CLASS = FlareEnv.TEST['CHATBOT']

    def __init__(self): pass

    def execute(self, command):
        if type(command) == list:
            command = " ".join(command)
        with settings(warn_only=True):
            run(command)

    def run_test(self, simulationClassList):
        if len(simulationClassList) < 0:
            print('No Simulation')
            return

        # cd gatling home
        with cd(FlareDeploy.REMOTE_GATLING_HOME):
            # maven test
            for simulationClass in simulationClassList:
                self.execute(self.MVN_TEST.format(simulationClass))

    def init_data(self):
        self.run_test(self.INIT_SIMULATION_CLASS)

    def talk_test(self):
        self.run_test(self.TALK_SIMULATION_CLASS)

    def scenario_talk_test(self):
        self.run_test(self.SCENARIO_TALK_SIMULATION_CLASS)

    def chatbot_talk_test(self):
        self.run_test(self.CHATBOT_TALK_SIMULATION_CLASS)