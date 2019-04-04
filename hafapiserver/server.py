# encoding = 'utf-8'

from flask import Flask
from flask_restful import abort, Api
from haf.ext.jinjia2report.report import Jinja2Report
from haf.config import *
from flask_restful import Resource
from hafapiserver.resources import *


app = Flask("haf-app")
api = Api(app)

sql_config = sql_config
mysql_tool = MysqlTool()


class HafApiServer(object):
    def __init__(self, args):
        self.args = args

    def run(self):
        print(self.args)
        app.run(debug=False, port=8888)


class ResultResource(Resource):
    def __init__(self):
        super().__init__()
        self.bus_client = BusClient()

    def get(self):
        result = self.mysql_tool.connect_execute(self.sql_config, sql_check, run_background=rb, commit=True)
        results = globalenv.get_global("results")
        if not get_queue.empty():
            results = get_queue.get()
            globalenv.set_global("results", results)

        return results.deserialize()


@app.route("/")
def index() -> str:
    return f"""
    <html>
    <pre>{BANNER_STRS}
    </pre>
    <html>"""