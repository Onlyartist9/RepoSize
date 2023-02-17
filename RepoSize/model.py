import argparse

#Making use of the argparse parser.
parser =argparse.ArgumentParser()

'''
What we want to design is a CLI that takes in commands in a myriad of ways.
The simple way simply accepts <owner>/<repo> and returns the size in a myriad of ways
(depending on file size it returns appropriate format(MB/KB/GB,etc))

We should also allow users to query private repos. In which context they'll need 
the private subcommand which comes with a switch allowing for the 
addition of a authentication token. 

We should also detail how a user may get an authentication token.

'''

#Adding a subcommand
parser.add_argument("repository")
parser.add_argument("-r","--repo",action="store_true")

arguments = parser.parse_args()
target_repo = arguments.repository

