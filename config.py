import os
import json

FLARE_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(FLARE_ROOT_PATH, 'conf/config.json')
print('load conig = ' + CONFIG_PATH)
with open(CONFIG_PATH, 'r') as f:
    Config = json.load(f)

class FlarePath:
    # FLARE HOME
    FLARE_HOME = FLARE_ROOT_PATH
    # WORKSPACE
    WORKSPACE = os.path.join(FLARE_HOME, Config['DIR']['WORKSPACE'])
    # WORKSPACE
    WORKSPACE_HOME = os.path.join(WORKSPACE, 'home')
    # TEMP HOME
    TEMP_HOME = os.path.join(FLARE_HOME, 'temp')
    # ORACLE HOME
    ORACLE_HOME = os.path.join(WORKSPACE, 'supertalk-99-release/target/enomix-oracle/enomix-oracle')
    # POSTGRESQL HOME
    POSTGRESQL_HOME = os.path.join(WORKSPACE, 'supertalk-99-release/target/enomix-postgresql/enomix-postgresql')


class FlareEnv():
    SVN = Config['SVN']
    DB = Config['DB']
    SOLR_URL = Config['SOLR']
    SERVER = Config['SERVER']


class FlareDocker():
    ENOMIX_NAME = 'eer'
    ENOMIX_HOME = '/home/enomix'


class FlareDeploy():
    DEPLOY_TEMP_PATH = FlarePath.TEMP_HOME + '/deploy'
    DEPLOY_TEMP_EER_PATH = os.path.join(DEPLOY_TEMP_PATH, 'eer')
    DEPLOY_TEMP_GATLING_PATH = os.path.join(DEPLOY_TEMP_PATH, 'gatling')

    DEPLOY_EER_TAR_NAME = 'enomix.tar'
    REMOTE_HOME = '/home/enomix/flare'