import os
import json

FLARE_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(FLARE_ROOT_PATH, 'flare_conf/config.json')
TEST_INFO_PATH = os.path.join(FLARE_ROOT_PATH, 'flare_conf/test_info.json')
PROCESS_PATH = os.path.join(FLARE_ROOT_PATH, 'flare_conf/process.json')

print('Load Conig = ' + CONFIG_PATH)
with open(CONFIG_PATH, 'r') as f:
    CONFIG = json.load(f)

print('Load Test Info = ' + TEST_INFO_PATH)
with open(TEST_INFO_PATH, 'r') as f:
    TEST_INFO = json.load(f)

print('Load Test Info = ' + PROCESS_PATH)
with open(PROCESS_PATH, 'r') as f:
    PROCESS = json.load(f)


class FlarePath:
    # FLARE HOME
    FLARE_HOME = FLARE_ROOT_PATH
    # FLARE_WORKSPACE
    FLARE_WORKSPACE = os.path.join(FLARE_HOME, CONFIG['DIR']['FLARE_WORKSPACE'])
    # FLARE_RESULT
    FLARE_RESULT = os.path.join(FLARE_HOME, CONFIG['DIR']['FLARE_RESULT'])
    # FLARE_FRAME
    FLARE_FRAME = os.path.join(FLARE_HOME, CONFIG['DIR']['FLARE_FRAME'])
    # TEMP HOME
    FLARE_TEMP = os.path.join(FLARE_HOME, CONFIG['DIR']['FLARE_TEMP'])
    # WORKSPACE
    PROJECT_EER_HOME = os.path.join(FLARE_WORKSPACE, 'home')
    # ORACLE HOME
    ORACLE_HOME = os.path.join(FLARE_WORKSPACE, 'supertalk-99-release/target/enomix-oracle/enomix-oracle')
    # POSTGRESQL HOME
    POSTGRESQL_HOME = os.path.join(FLARE_WORKSPACE, 'supertalk-99-release/target/enomix-postgresql/enomix-postgresql')


class FlareEnv():
    SVN = CONFIG['SVN']
    DB = CONFIG['DB']
    SOLR_URL = CONFIG['SOLR']
    SERVER = CONFIG['SERVER']
    SCOUTER = CONFIG['SCOUTER']
    GATLING = CONFIG['GATLING']


class FlareDocker():
    ENOMIX_NAME = 'eer'
    ENOMIX_HOME = '/home/enomix'
    PORT = {
        'GATEWAY': [19010, 19010],
        'WEBAPPS': [19090, 19090],
        'WEBROOT': [17070, 17070],
        'SCOUTER': [6100, 6100]
    }


class FlareProcess():
    BUILD = PROCESS['BUILD']
    DEPLOY = PROCESS['DEPLOY']
    TEST = PROCESS['TEST']
    REPORT = PROCESS['REPORT']


class FlareDeploy():
    DEPLOY_TEMP_PATH = FlarePath.FLARE_TEMP + '/deploy'
    DEPLOY_TEMP_EER_PATH = os.path.join(DEPLOY_TEMP_PATH, 'eer')
    DEPLOY_TEMP_GATLING_PATH = os.path.join(DEPLOY_TEMP_PATH, 'gatling')

    DEPLOY_EER_TAR_NAME = 'enomix.tar'
    REMOTE_HOME = '/home/enomix/flare'
    REMOTE_ENOMIX_ORACLE_HOME = os.path.join(REMOTE_HOME, 'enomix-oracle')
    REMOTE_GATLING_HOME = os.path.join(REMOTE_HOME, 'flare-gatling')


class FlareTest():
    TEST_MODULE = {
        'SETUP': 'N',
        'UNIT': 'N',
        'SPRINT': 'N',
        'PRODUCT': 'Y'
    }
    SETUP = TEST_INFO['SETUP']
    UNIT_TEST = TEST_INFO['UNIT_TEST']
    SPRINT_TEST = TEST_INFO['SPRINT_TEST']
    PRODUCT_TEST = TEST_INFO['PRODUCT_TEST']


class FlareResult():
    REMOTE_GATLING_HOME = FlareDeploy.REMOTE_GATLING_HOME
    REMOTE_GATLING_RESULT = os.path.join(REMOTE_GATLING_HOME, 'target/gatling')


class FlareWeb():
    PORT =CONFIG['WEB']["PORT"]