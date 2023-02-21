# RepoSize
A command line tool that returns the size of a specified repo.

The main reason I am creating this tool is due to the fact that I realized it's fairly opaque finding out the size of a repo. 

This can be important in data constrained environments (like a case in which a user has a data use limit) and needs to pull a repository. Finding out the size of repository can save costs before pulling a repo.

# Make sure you're using python version 3.6

# Currently only works for public repositories.

## Installation

```console
# clone the repo
$ git clone https://github.com/Onlyartist9/RepoSize.git

# change the working directory to RepoSize
$ cd RepoSize

# install the requirements
$ python3 -m pip install -r requirements.txt
```

## Usage
```console
python reposize nameofuser/nameofrepository
```
