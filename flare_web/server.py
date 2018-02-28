from flask import Flask, views, render_template
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from config import FlarePath, FlareWeb
from flare_web.api.report import Report

class FlareView(views.View):
    def __init__(self, template_name):
        self.template_name = template_name
    def dispatch_request(self):
        return render_template(self.template_name, flower="")

# Define
app = Flask(__name__, static_folder=FlarePath.FLARE_RESULT, static_url_path='', template_folder=FlarePath.FLARE_RESULT)
app.debug = True
report = Report()

# Router
app.add_url_rule('/', view_func=FlareView.as_view('index', template_name='index.html'))
app.add_url_rule('/api/report', view_func=report.selectType)
app.add_url_rule('/api/report/<type>', view_func=report.selectDate)
app.add_url_rule('/api/report/<type>/<date>', view_func=report.selectReport)

# Main
if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(FlareWeb.PORT)
    print('Server Start {0}'.format(FlareWeb.PORT))
    IOLoop.instance().start()
