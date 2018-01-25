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



class FlareEnv(FlarePath):
    SVN = [
        Config['SVN']['ID'],
        Config['SVN']['PASSWORD'],
        Config['SVN']['URL'],
        FlarePath.WORKSPACE
    ]

    DB_ORACLE = [
        Config['DB']['ORACLE']['DRIVER'],
        Config['DB']['ORACLE']['URL'],
        Config['DB']['ORACLE']['USERNAME'],
        Config['DB']['ORACLE']['PASSWORD'],
        Config['DB']['ORACLE']['OWNERNAME'],
        Config['DB']['ORACLE']['VALIDATION']
    ]

    DB_POSTGRESQL = [
        Config['DB']['POSTGRESQL']['DRIVER'],
        Config['DB']['POSTGRESQL']['URL'],
        Config['DB']['POSTGRESQL']['USERNAME'],
        Config['DB']['POSTGRESQL']['PASSWORD'],
        Config['DB']['POSTGRESQL']['OWNERNAME'],
        Config['DB']['POSTGRESQL']['VALIDATION']
    ]

    SOLR_ORACLE_URL = Config['SOLR']['ORACLE']
    SOLR_POSTGRESQL_URL = Config['SOLR']['POSTGRESQL']

    SERVER = Config['SERVER']