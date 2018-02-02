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

    def clean(self):
        self.move_maven_root()
        subprocess.call(self.MVN_CLEAN, shell=True)

    def install(self):
        self.move_maven_root()
        subprocess.call(self.MVN_INSTALL, shell=True)

    def clean_install(self):
        self.clean()
        self.install()

    def database_clean(self):
        self.move_maven_root()
        subprocess.call(self.MVN_TEST_DB_CLEAN, shell=True)