import os
import wget
from fabric.api import *
from config import FlarePath, FlareEnv

class Scouter():

    SCOUTER_SETUP = [
        FlarePath.TEMP_HOME + '/scouter',
        FlareEnv.SCOUTER["DOWNLOAD_URL"],
        FlarePath.ORACLE_HOME + '/scouter'
    ]

    STORE_SCOUTER_CONF_PATH = [
        FlareEnv.STORE["PATH"] + '/scouter/conf',
        FlarePath.TEMP_HOME + '/scouter/agent.java/conf',
    ]

    def __init__(self):
        tempDir = [
            '/scouter'
        ]
        # create temp directory
        for dir in tempDir:
            path = FlarePath.TEMP_HOME + dir
            if not os.path.exists(path):
                os.makedirs(path)

        self.scouterTarName = self.SCOUTER_SETUP[1][self.SCOUTER_SETUP[1].rfind('/') + 1:]

    def agent_set(self):
        self.download()
        self.deploy_agent()

    def download(self):
        scouterTarPath = self.SCOUTER_SETUP[0] + '/' + self.scouterTarName
        if os.path.isfile(scouterTarPath):
            return

        with lcd(self.SCOUTER_SETUP[0]):
            local('rm -rf *')

        print('Download scouter: {0}'.format(self.SCOUTER_SETUP[1]))
        wget.download(self.SCOUTER_SETUP[1], self.SCOUTER_SETUP[0])

        with lcd(self.SCOUTER_SETUP[0]):
            local('tar -xf {0}'.format(self.scouterTarName))
            local('mv ./scouter/* .')
            local('rmdir scouter')

        local('cp {0}/* {1}/'.format(self.STORE_SCOUTER_CONF_PATH[0], self.STORE_SCOUTER_CONF_PATH[1]))


    def deploy_agent(self):
        if os.path.exists(self.SCOUTER_SETUP[2]):
            with lcd(self.SCOUTER_SETUP[2]):
                local('rm -rf *')

        for scouterModule in ['/agent.java', '/agent.host']:
            scouterPath = self.SCOUTER_SETUP[0] + scouterModule
            deployPath = self.SCOUTER_SETUP[2] + scouterModule
            local('mkdir -p {0}'.format(deployPath))
            local('cp -r {0} {1}'.format(scouterPath, deployPath))
