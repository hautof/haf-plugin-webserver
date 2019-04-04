# encoding = 'utf-8'

from haf.config import *
from hafapiserver.server import HafApiServer
import argparse


def init():
    print(BANNER_STRS)


def main_args():

    init()

    arg_program = argparse.ArgumentParser(prog="python -m hafapiserver", add_help=True)

    sub_all_arg_program = arg_program.add_subparsers(dest="all")

    sub_run_arg_program = sub_all_arg_program.add_parser("run",
                                                         help="run case, using `python -m hafapiserver run ` or `python -m hafapiserver` to run all case in local path ")
    args = arg_program.parse_args()
    # name
    sub_run_arg_program.add_argument("--name", "-name", dest="name", type=str, default="AutoTest",
                                     help="test name, defautl is autotest")
    has = HafApiServer(args)
    has.run()


main_args()