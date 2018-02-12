import os
import json

FLARE_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(FLARE_ROOT_PATH, 'flare_conf/config.json')
print('load conig = ' + CONFIG_PATH)
with open(CONFIG_PATH, 'r') as f:
    Config = json.load(f)

class FlarePath:
    # FLARE HOME
    FLARE_HOME = FLARE_ROOT_PATH
    # FLARE_WORKSPACE
    FLARE_WORKSPACE = os.path.join(FLARE_HOME, Config['DIR']['FLARE_WORKSPACE'])
    # FLARE_FRAME
    FLARE_FRAME = os.path.join(FLARE_HOME, Config['DIR']['FLARE_FRAME'])
    # TEMP HOME
    FLARE_TEMP = os.path.join(FLARE_HOME, Config['DIR']['FLARE_TEMP'])
    # WORKSPACE
    PROJECT_EER_HOME = os.path.join(FLARE_WORKSPACE, 'home')
    # ORACLE HOME
    ORACLE_HOME = os.path.join(FLARE_WORKSPACE, 'supertalk-99-release/target/enomix-oracle/enomix-oracle')
    # POSTGRESQL HOME
    POSTGRESQL_HOME = os.path.join(FLARE_WORKSPACE, 'supertalk-99-release/target/enomix-postgresql/enomix-postgresql')


class FlareEnv():
    SVN = Config['SVN']
    DB = Config['DB']
    SOLR_URL = Config['SOLR']
    SERVER = Config['SERVER']
    SCOUTER = Config['SCOUTER']
    GATLING = Config['GATLING']


class FlareDocker():
    ENOMIX_NAME = 'eer'
    ENOMIX_HOME = '/home/enomix'
    PORT = {
        'GATEWAY': [19010, 19010],
        'WEBAPPS': [19090, 19090],
        'WEBROOT': [17070, 17070],
        'SCOUTER': [6100, 6100]
    }

class FlareDeploy():
    DEPLOY_TEMP_PATH = FlarePath.FLARE_TEMP + '/deploy'
    DEPLOY_TEMP_EER_PATH = os.path.join(DEPLOY_TEMP_PATH, 'eer')
    DEPLOY_TEMP_GATLING_PATH = os.path.join(DEPLOY_TEMP_PATH, 'gatling')

    DEPLOY_EER_TAR_NAME = 'enomix.tar'
    REMOTE_HOME = '/home/enomix/flare'
    REMOTE_ENOMIX_ORACLE_HOME = os.path.join(REMOTE_HOME, 'enomix-oracle')
    REMOTE_GATLING_HOME = os.path.join(REMOTE_HOME, 'flare-gatling')