import os
import wget
from fabric.api import *
from config import FlareEnv, FlareDeploy, FlarePath
from decorator import before, remote

@before(remote(FlareEnv.SERVER["GATLING"]))
class Init():

    MVN_TEST = 'mvn -Dtest=FlareParam -DsimulationClass={0} test'

    SIMULATION_CLASS = FlareEnv.TEST['INIT']

    def __init__(self): pass


    def execute(self, command):
        if type(command) == list:
            command = " ".join(command)
        with settings(warn_only=True):
            run(command)


    def init_data(self):
        # cd gatling home
        with cd(FlareDeploy.REMOTE_GATLING_HOME):
            # maven test
            for simulationClass in self.SIMULATION_CLASS:
                self.execute(self.MVN_TEST.format(simulationClass))
