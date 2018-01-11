import os
import subprocess
from config import FlarePath

class Maven():

    MVN_CLEAN = 'mvn clean '

    MVN_INSTALL = 'mvn install -Drelease.skip=false -Drelease.oracle.skip=false -Drelease.mssql.skip=true -Drelease.postgresql.skip=false'

    def __init__(self):
        pass

    def move_maven_root(self):
        os.chdir(FlarePath.WORKSPACE)

    def clean(self):
        self.move_maven_root()
        subprocess.call(self.MVN_CLEAN, shell=True)

    def install(self):
        self.move_maven_root()
        subprocess.call(self.MVN_INSTALL, shell=True)

    def clean_install(self):
        self.clean()
        self.install()