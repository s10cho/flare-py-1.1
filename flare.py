import os
import sys
import importlib
import traceback

def main():
    args = sys.argv[1:]
    if args[0] == 'help':
        moduleList = os.listdir('flare_module')
        helpMessage = [
            '\n',
            'Usage:\n',
            '    python3 flare.py [command]\n\n',
            'Commands:\n'
        ]
        for moduleName in moduleList:
            if moduleName.isalpha():
                helpMessage.append('    {0}\n'.format(moduleName))
        print(''.join(helpMessage))
    else:
        try:
            moduleName = args[0]
            ClassName = moduleName.title() + 'Service'
            module = importlib.import_module('flare_module.{0}.service'.format(moduleName))
            Class = getattr(module, ClassName)
            instance = Class()
            instance.run()
        except Exception:
            print(traceback.format_exc())



if __name__ == '__main__':
    main()