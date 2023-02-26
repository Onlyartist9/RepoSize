import argparse
import re
import sys

parser =argparse.ArgumentParser(prog="reposize",description="Find the size of the specifed Github repository. Used this way: python reposize lucidrains/toolformer-pytorch",epilog="Thanks for using %(prog)s!")

parser.add_argument("repository")
parser.add_argument("-v","--version",action="version",version="%(prog)s 1.1.1")

arguments = parser.parse_args()
target_repo = arguments.repository

pattern = "^[a-zA-Z0-9_.-]+\/[a-zA-Z0-9_.-]+$"

match = re.match(pattern, target_repo)
try:
    if not match:
        raise ValueError("Invalid input")
except ValueError as e:
    print(e)
    print("Please enter a valid Github repository in the form <user>/<repository>")
    sys.exit(1)


