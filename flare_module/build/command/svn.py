import subprocess
from config import FlarePath, FlareEnv

class Svn():

    SVN_CHECKOUT = [
        'svn checkout',
        '--username {0}'.format(FlareEnv.SVN['ID']),
        '--password {0}'.format(FlareEnv.SVN['PASSWORD']),
        '{0}'.format(FlareEnv.SVN['URL']),
        '{0}'.format(FlarePath.WORKSPACE)
    ]

    def __init__(self): pass

    def checkout(self):
        self.call(self.SVN_CHECKOUT)

    def call(self, command):
        if type(command) == str:
            cmd = command
        else:
            cmd = " ".join(command)
        print(cmd)
        subprocess.call(cmd, shell=True)