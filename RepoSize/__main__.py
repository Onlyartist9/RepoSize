#! /usr/bin/env python3

"""
Returns the size of a particular Github Repository.
"""

import sys


if __name__ == "__main__":
    # Check if the user is using the correct version of Python
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 6):
        print("Reposize requires Python 3.6+\nYou are using Python %s, which is not supported by Reposize" % (python_version))
        sys.exit(1)

    import reposize
    
    reposize