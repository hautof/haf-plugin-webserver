# encoding = 'utf-8'

from flask import Flask
from flask_restful import abort, Api
from haf.busclient import BusClient
from haf.ext.jinjia2report.report import Jinja2Report
from haf.config import *
from hafapiserver.resources import *

app = Flask("haf-app")
api = Api(app)


@app.route("/")
def index() -> str:
    return f"""
    <html>
    <pre>{BANNER_STRS}
    </pre>
    <html>"""


@app.route("/report")
def report() -> str:
    ResultResource().get()
    report_stream = Jinja2Report.report_online(globalenv.get_global("results"))
    return report_stream
    
@app.route("/report-app")
def report_app() -> str:
    ResultResource().get()
    report_stream = Jinja2Report.report_online_app(globalenv.get_global("results"))
    return report_stream

@app.route("/report-web")
def report_web() -> str:
    ResultResource().get()
    report_stream = Jinja2Report.report_online_app(globalenv.get_global("results"))
    return report_stream

@app.route("/status")
def status() -> str:
    return '{"status": "ok"}'

def abort_if_not_exist():
    abort(404, message="404")


def web_server(bus_client: BusClient):
    bus_client = BusClient(bus_client.domain, bus_client.port, bus_client.auth_key)
    api.add_resource(LoaderResource, "/loader")
    api.add_resource(RunnerResource, "/runner")
    api.add_resource(ResultResource, "/result")
    api.add_resource(DocResource, "/doc")
    app.run(debug=False, port=WEB_SERVER_PORT)


