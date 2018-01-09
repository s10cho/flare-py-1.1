import json

class Config():
    with open('conf/config.json', 'r') as f:
        config = json.load(f)

    def getConfig(self):
        return self.config

class Command():
    # svn command
    SVN_CHECKOUT = 'svn checkout --username {0} --password {1} {2} {3}'

    # maven command
    MVN_CLEAN_INSTALL = 'mvn clean install'

    MVN_TEST_DB_CLEAN = 'mvn test -DskipTests=false -Dtest=spectra.ee.test.webapps.DropTestData -DfailIfNoTests=false'