import os
import wget
from fabric.api import *
from config import FlarePath, FlareEnv

class Scouter():

    SCOUTER_SETUP = [
        FlarePath.TEMP_HOME + '/scouter',
        FlareEnv.SCOUTER["DOWNLOAD_URL"],
        FlarePath.ORACLE_HOME + '/lib'
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

    def agent_set(self):
        self.download()
        self.untar()
        self.deploy_agent()

    def download(self):
        scouterPath = self.SCOUTER_SETUP[0] + '/agent.java'
        if not os.path.exists(scouterPath):
            print('Download scouter: {0}'.format(self.SCOUTER_SETUP[1]))
            wget.download(self.SCOUTER_SETUP[1], self.SCOUTER_SETUP[0])


    def untar(self):
        scouterPath = self.SCOUTER_SETUP[0]
        downloadUrl = self.SCOUTER_SETUP[1]
        fileName = downloadUrl[downloadUrl.rfind('/') + 1:]
        with lcd(scouterPath):
            local('tar -xf {0}'.format(fileName))
            local('mv ./scouter/* .')
            local('rmdir scouter')


    def deploy_agent(self):
        scouterPath = self.SCOUTER_SETUP[0] + '/agent.java'
        if os.path.exists(scouterPath):
            local('cp -r {0} {1}'.format(scouterPath, self.SCOUTER_SETUP[2]))
