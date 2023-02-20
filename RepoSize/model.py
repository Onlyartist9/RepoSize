import argparse

parser =argparse.ArgumentParser(prog="reposize",description="Find the size of the specifed Github repository. Used this way: python reposize lucidrains/toolformer-pytorch",epilog="Thanks for using %(prog)s!")

parser.add_argument("<user/repo>")
parser.add_argument("-v","--version",action="version",version="%(prog)s 1.0.0")

arguments = parser.parse_args()
target_repo = arguments.repository

