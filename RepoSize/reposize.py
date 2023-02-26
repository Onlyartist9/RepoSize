import requests
import model

def requester(request):
    
    response = requests.get(
        "https://api.github.com/repos/"+str(request)
    )
  
    json_response = response.json()
    size = json_response['size']
    return size

def displayer(size):
    if size >= 1000:
        sizeinMB = size/1000
        print(f"The repository's size is {sizeinMB} MB",)
    elif size >= 10**6:
        sizeinGB = size/10**6
        print("The repository's size is {sizeinGB} GB",)

reporequest = model.target_repo

request = requester(reporequest)
displayer(request)