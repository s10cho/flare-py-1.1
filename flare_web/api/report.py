import os
from flask import jsonify
from config import FlarePath


class Report():

    REPORT_ROOT = FlarePath.FLARE_RESULT + '/report'
    REPORT_TYPE = REPORT_ROOT + '/{0}'
    REPORT_DATE = REPORT_ROOT + '/{0}/{1}'

    def list(self, path, reverse):
        data = os.listdir(path)
        data.sort(reverse=reverse)

        return jsonify({
            'data': data
        })

    def selectType(self):
        return self.list(self.REPORT_ROOT, False)

    def selectDate(self, type):
        return self.list(self.REPORT_TYPE.format(type), True)

    def selectReport(self, type, date):
        return self.list(self.REPORT_DATE.format(type, date), False)

    def view(self, type, date, view):
        return view