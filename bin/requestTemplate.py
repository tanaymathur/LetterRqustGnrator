__author__ = 'knight'

import requests
import json

headers = {'content-type': 'application/json'}
url = 'http://192.168.3.45:8080/api/v2/event/log'
username = 'svc_client'
password = 'password'

def post(payloadData):
    response = requests.posts(url,data=payloadData,headers=headers,auth = (username,password))

def request(data):
    response =  post(json.loads(data))
    print(response.status)
