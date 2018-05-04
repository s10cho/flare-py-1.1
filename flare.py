import os
import sys
import importlib
import traceback
from config import CONFIG

def main():
    args = sys.argv[1:]
    if args[0] == 'help':
        moduleList = os.listdir('flare_module')
        helpMessage = [
            '\n',
            'Usage:\n',
            '    python3 flare.py [module]\n\n',
            'Modules:\n'
        ]
        for moduleName in moduleList:
            if moduleName.isalpha():
                helpMessage.append('    {0}\n'.format(moduleName))
        print(''.join(helpMessage))
    else:
        try:
            moduleName = args[0]
            param = args[1:]
            ClassName = moduleName.title() + 'Service'
            module = importlib.import_module('{0}.{1}.service'.format(CONFIG['DIR']['FLARE_MODULE'], moduleName))
            Class = getattr(module, ClassName)
            instance = Class()
            instance.run(param)
        except Exception:
            print(traceback.format_exc())

if __name__ == '__main__':
    main()