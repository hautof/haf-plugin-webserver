from hafsqlpublish.publish import Publish
from multiprocessing import Process
import haf


@haf.hookimpl
def add_option(parse):
    """Here the caller expects us to return a list."""
    parse.add_argument("--web-server", "-ws", type=bool,
                        help="""default is not run;
                            if is True, would create web server to offer the api and html service;""")
    return parse


@haf.hookimpl
def start_web_server(args, bus_client):
    if hasattr(args, 'web_server') and args.web_server:
        try:
            from hafapiserver.app import web_server
            ws = Process(target=web_server, args=(bus_client,), daemon=True)
            ws.start()
            return True
        except Exception as e:
            print(e)
    return False