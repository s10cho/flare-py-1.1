import subprocess
from flare_module.common.config import FlareEnv

class Svn():

    SVN_CHECKOUT = 'svn checkout --username {0} --password {1} {2} {3}'

    def __init__(self):
        self.svn = FlareEnv.svn


    def checkout(self):
        command = self.SVN_CHECKOUT.format(self.svn[0], self.svn[1], self.svn[2], self.svn[3])
        print(command)
        subprocess.call(command, shell=True)
