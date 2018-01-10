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
    MVN_CLEAN_INSTALL = 'mvn clean install -Drelease.skip=false -Drelease.oracle.skip=false -Drelease.mssql.skip=true -Drelease.postgresql.skip=false'
    MVN_TEST_DB_CLEAN = 'mvn test -DskipTests=false -Dtest=spectra.ee.test.webapps.DropTestData -DfailIfNoTests=false'

    # ant command
    ANT_COMMAND = ''

class Template():

    JDBC = 'engine.properties.oracle'
    SETUP = 'setup.properties'

    def get_template(self, template_name):
        template_path = 'template/' + template_name
        with open(template_path, 'r', encoding='UTF8') as f:
            template = f.read()

        return template
