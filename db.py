import sys
import shutil
from props import Config, Formmat

class DB():
    def __init__(self):
        config = Config().getConfig()

        self.oracle = [
            config['ORACLE_DB']['DRIVER'],
            config['ORACLE_DB']['URL'],
            config['ORACLE_DB']['T']['USERNAME'],
            config['ORACLE_DB']['T']['PASSWORD'],
            config['ORACLE_DB']['T']['OWNERNAME'],
            config['ORACLE_DB']['VALIDATION']
        ]

        self.jdbc_file = [
            config['DIR']['JDBC']['TEMP_PATH'],
            config['DIR']['JDBC']['COPY_PATH']
        ]

    def jdbc_init(self):
        self.jdbc_convert()
        self.jdbc_copy()

    def jdbc_convert(self):
        jdbc = Formmat.JDBC.format(self.oracle[0], self.oracle[1], self.oracle[2], self.oracle[3],self.oracle[4], self.oracle[5])
        f = open(self.jdbc_file[0], 'w')
        f.write(jdbc)
        f.close()

    def jdbc_copy(self):
        shutil.copy(self.jdbc_file[0], self.jdbc_file[1])




def main():
    args = sys.argv[1:]

    db = DB()
    if args[0] == 'init':
        db.jdbc_init()
        del args[0]


if __name__ == '__main__':
    main()