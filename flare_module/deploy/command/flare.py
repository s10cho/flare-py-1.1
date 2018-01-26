from fabric.api import *
from config import FlarePath, FlareEnv
from decorator import before, remote

#@before(remote(FlareEnv.SERVER["FLARE"]))
class FlareServer():

    def __init__(self): pass

    def execute(self, command):
        run(command)

    def compress(self):
        local('mkdir -p {0}/{1}'.format(FlarePath.TEMP_HOME, 'deploy'))

        with cd(FlarePath.ORACLE_HOME):
            local('ls')
