import os
from flask import jsonify
from config import FlarePath


class Report():

    REPORT_ROOT = FlarePath.FLARE_RESULT + '/report'
    REPORT_TYPE = REPORT_ROOT + '/{0}'
    REPORT_DATE = REPORT_ROOT + '/{0}/{1}'

    def listDir(self, path):
        return os.listdir(path)

    def selectType(self):
        typeList = self.listDir(self.REPORT_ROOT)
        return jsonify({
            'data': typeList
        })

    def selectDate(self, type):
        dateList = self.listDir(self.REPORT_TYPE.format(type))
        dateList.sort(reverse=True)
        return jsonify({
            'data': dateList
        })

    def selectTest(self, type, date):
        testList = self.listDir(self.REPORT_DATE.format(type, date))
        testList.sort(key=lambda x: x[-14:], reverse=True)
        return jsonify({
            'data': testList
        })