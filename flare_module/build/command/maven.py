import os
import subprocess
from config import FlarePath

class Maven():

    MVN_CLEAN = 'mvn clean'

    MVN_INSTALL = 'mvn install -Drelease.skip=false -Drelease.oracle.skip=false -Drelease.mssql.skip=true -Drelease.postgresql.skip=false'

    MVN_TEST_DB_CLEAN = 'mvn test -DskipTests=false -Dtest=spectra.ee.test.webapps.DropTestData -DfailIfNoTests=false -Dbuild.service.license=basic'

    def __init__(self): pass

    def move_maven_root(self):
        os.chdir(FlarePath.FLARE_WORKSPACE)

    def clean_install(self):
        self.clean()
        self.install()

    def clean(self):
        self.move_maven_root()
        self.execute(self.MVN_CLEAN)

    def install(self):
        self.move_maven_root()
        self.execute(self.MVN_INSTALL)

    def database_clean(self):
        self.move_maven_root()
        self.execute(self.MVN_TEST_DB_CLEAN)

    def execute(self, command):
        if type(command) == list:
            command = " ".join(command)
            subprocess.call(command, shell=True)
