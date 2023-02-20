import argparse

'''
What we want to design is a CLI that takes in commands in a myriad of ways.
The simple way simply accepts <owner>/<repo> and returns the size in a myriad of ways
(depending on file size it returns appropriate format(MB/KB/GB,etc))

We should also allow users to query private repos. In which context they'll need 
the private subcommand which comes with a switch allowing for the 
addition of a authentication token. 

We should also detail how a user may get an authentication token in a help section that can be activated when the file alone is used.

command for basic query search should be simply

General purpose query:
python reposize <owner>/<repo>

Private repo query
python reposize private -t <token> <owner>/<repo>
'''

#Making use of the argparse parser.
parser =argparse.ArgumentParser(prog="reposize",description="Find the size of the specifed Github repository.",epilog="Thanks for using %(prog)s!")
subparser = parser.add_subparsers(title="subcommand", help ="In case you need to find the size of one of your own repos you'll need an authentication token.Once you have that though use this subcommand to enter the token and access it.")
#Adding a subcommand
parser.add_argument("repository")

arguments = parser.parse_args()
target_repo = arguments.repository

