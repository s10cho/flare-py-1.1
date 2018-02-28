import os
from flask import jsonify
from config import FlarePath


class Report():

    REPORT_ROOT = FlarePath.FLARE_RESULT + '/report'
    REPORT_TYPE = REPORT_ROOT + '/{0}'
    REPORT_DATE = REPORT_ROOT + '/{0}/{1}'

    def list(self, path):
        data = os.listdir(path)
        result = {
            'data': data
        }
        return jsonify(result)

    def selectType(self):
        return self.list(self.REPORT_ROOT)

    def selectDate(self, type):
        return self.list(self.REPORT_TYPE.format(type))

    def selectReport(self, type, date):
        return self.list(self.REPORT_DATE.format(type, date))

    def view(self, view):
        return view