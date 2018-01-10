import sys
from command.svn import Svn

def main():
    args = sys.argv[1:]

    svn = Svn()
    if args[0] == 'checkout':
        svn.checkout()
        del args[0]

if __name__ == '__main__':
    main()