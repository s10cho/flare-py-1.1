import os
import sys
import importlib

def main():
    args = sys.argv[1:]
    if args[0] == 'help':
        moduleList = os.listdir('flare_module')
        print('Usage:')
        print('    python3 flare.py [command]')
        print('Commands:')
        for moduleName in moduleList:
            if moduleName.isalpha():
                print('    {0}'.format(moduleName))
        pass
    else:
        moduleName = args[0]
        ClassName = moduleName.title() + 'Service'
        module = importlib.import_module('flare_module.{0}.service'.format(moduleName))
        Class = getattr(module, ClassName)
        instance = Class()
        instance.run()


if __name__ == '__main__':
    main()