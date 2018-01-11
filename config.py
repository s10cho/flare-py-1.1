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
    # TEMP HOME
    TEMP_HOME = os.path.join(WORKSPACE, 'temp')
    # ORACLE HOME
    ORACLE_HOME = os.path.join(WORKSPACE, 'supertalk-99-release/target/enomix-oracle/enomix-oracle')
    # POSTGRESQL HOME
    POSTGRESQL_HOME = os.path.join(WORKSPACE, 'supertalk-99-release/target/enomix-postgresql/enomix-postgresql')



class FlareEnv(FlarePath):
    svn = [
        Config['SVN']['ID'],
        Config['SVN']['PASSWORD'],
        Config['SVN']['URL'],
        FlarePath.WORKSPACE
    ]