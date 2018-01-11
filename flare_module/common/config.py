import os
import json
import flare

config_path = os.path.join(flare.FLARE_HOME, 'conf/config.json')
print('load conig = ' + config_path)
with open(config_path, 'r') as f:
    Config = json.load(f)

class FlarePath:

    FLARE_ROOT = flare.FLARE_HOME

    WORKSPACE = os.path.join(FLARE_ROOT, Config['DIR']['WORKSPACE'])


class FlareEnv(FlarePath):
    svn = [
        Config['SVN']['ID'],
        Config['SVN']['PASSWORD'],
        Config['SVN']['URL'],
        FlarePath.WORKSPACE
    ]