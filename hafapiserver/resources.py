# encoding='utf-8'
import requests
from haf import globalenv
from haf.busclient import BusClient
from haf.result import EndResult
from flask import make_response
from flask_restful import Resource

globalenv._init()
globalenv.set_global("runners", {})
globalenv.set_global("results", EndResult())


class CaseResource(Resource):
    def __init__(self):
        super().__init__()
        self.bus_client = BusClient()

    def get(self):
        pass


class ResultResource(Resource):
    def __init__(self):
        super().__init__()
        self.bus_client = BusClient()

    def get(self):
        get_queue = self.bus_client.get_publish_result()
        results = globalenv.get_global("results")
        if not get_queue.empty():
            results = get_queue.get()
            globalenv.set_global("results", results)

        return results.deserialize()


class RunnerResource(Resource):
    def __init__(self):
        super().__init__()
        self.bus_client = BusClient()

    def get(self):
        get_queue = self.bus_client.get_publish_runner()
        runners = globalenv.get_global("runners")
        if not get_queue.empty():
            runner = get_queue.get()
            runners[runner.get("key")] = runner
            globalenv.set_global("runners", runners)
        return globalenv.get_global("runners")


class LoaderResource(Resource):
    def __init__(self):
        super().__init__()
        self.bus_client = BusClient()

    def get(self):
        get_queue = self.bus_client.get_publish_loader()
        if not get_queue.empty():
            loader = get_queue.get()
            globalenv.set_global("loader", loader)
        return globalenv.get_global("loader")


class DocResource(Resource):
    def __init__(self):
        super().__init__()
        self.bus_client = BusClient()

    def get(self):
        return make_response(requests.get("http://autotest.wang").text, 200)
