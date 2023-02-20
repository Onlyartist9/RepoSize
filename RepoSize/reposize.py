import requests
import model

def requester(request):
    """validate value of request value: should be user/repo
    Probably making use of a regular expression. should probably look into if
    Github has a specifc format for user/repo.
    """
    response = requests.get(
        "https://api.github.com/repos/"+"request"
    )
    #Handles requests and parses said request
    json_response = response.json()
    size = json_response['size']
    return size

def displayer(size):
    if size >= 1000:
        sizeinMB = size/1000
        print("Your size is %f MB",sizeinMB)
    elif size >= 10**6:
        sizeinGB = size/10**6
        print("Your size is %f GB",sizeinGB)

reporequest = model.target_repo

request = requester(reporequest)
displayer(request)