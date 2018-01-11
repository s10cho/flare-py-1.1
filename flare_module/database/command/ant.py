import os
import subprocess
from config import FlarePath

class Ant():

    ANT = 'ant'
    SETUP_PATH = FlarePath.ORACLE_HOME + '/setup'

    def __init__(self):
        pass

    def build(self):
        self.move_maven_root()
        subprocess.call(self.ANT, shell=True)

    def move_maven_root(self):
        os.chdir(self.SETUP_PATH)