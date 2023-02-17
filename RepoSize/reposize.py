import requests
import model
import json

reporequest = model.target_repo

def requester(reporequest):
    #Handles requests and parses said request
    return size


def displayer(size):
    if size >= 1000:
        sizeinMB = size/1000
        print("Your size is %f MB",sizeinMB)
    elif size >= 10**6:
        sizeinGB = size/10**6
        print("Your size is %f MB",sizeinGB)

request = requester(reporequest)
displayer(request)