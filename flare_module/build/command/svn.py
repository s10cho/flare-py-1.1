import subprocess
from config import FlarePath, FlareEnv

class Svn():

    REMOVE_WORKSPASE_DIR = [
        'sudo rm -rf',
        '{0}'.format(FlarePath.FLARE_WORKSPACE)
    ]

    SVN_CHECKOUT = [
        'svn checkout',
        '--username {0}'.format(FlareEnv.SVN['ID']),
        '--password {0}'.format(FlareEnv.SVN['PASSWORD']),
        '{0}'.format(FlareEnv.SVN['URL']),
        '{0}'.format(FlarePath.FLARE_WORKSPACE)
    ]

    def __init__(self): pass

    def checkout(self):
        self.execute(self.REMOVE_WORKSPASE_DIR)
        self.execute(self.SVN_CHECKOUT)

    def execute(self, command):
        if type(command) == list:
            command = " ".join(command)
        subprocess.call(command, shell=True)
