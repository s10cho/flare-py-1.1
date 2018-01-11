import os
import json

FLARE_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(FLARE_ROOT_PATH, 'conf/config.json')
print('load conig = ' + config_path)
with open(config_path, 'r') as f:
    Config = json.load(f)

class FlarePath:

    FLARE_HOME = FLARE_ROOT_PATH

    WORKSPACE = os.path.join(FLARE_HOME, Config['DIR']['WORKSPACE'])


class FlareEnv(FlarePath):
    svn = [
        Config['SVN']['ID'],
        Config['SVN']['PASSWORD'],
        Config['SVN']['URL'],
        FlarePath.WORKSPACE
    ]