import os
import subprocess
from config import FlarePath

class Maven():

    MVN_TEST_DB_CLEAN = 'mvn test -DskipTests=false -Dtest=spectra.ee.test.webapps.DropTestData -DfailIfNoTests=false'

    def __init__(self):
        pass

    def move_maven_root(self):
        os.chdir(FlarePath.WORKSPACE)

    def db_clean(self):
        self.move_maven_root()
        subprocess.call(self.MVN_TEST_DB_CLEAN, shell=True)
