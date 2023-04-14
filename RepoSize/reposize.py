import sys
import requests
import model

def requester(request):

    response = requests.get(
        "https://api.github.com/repos/"+str(request)
    )
    
    json_response = response.json()
    try:
        size = json_response['size']
        if not size:
            raise KeyError("Missing Repo")
    except KeyError as e:
        print(e)
        print("Please enter a valid(make sure it exists and check typos) Github repository in the form <user>/<repository>")
        sys.exit(1)

    return size

def displayer(size):
    if size >= 1000:
        sizeinMB = size/1000
        print(f"The repository's size is {sizeinMB} MB")
    elif size >= 1000000:
        sizeinGB = size/1000000
        print(f"The repository's size is {sizeinGB} GB")
    else:
        print(f"The repository's size is {size} KB")

reporequest = model.target_repo

request = requester(reporequest)
displayer(request)