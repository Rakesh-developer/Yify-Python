import requests
import json
BASE_URL="https://api.themoviedb.org/3"

class Request():
    def __init__(self,api_key,url=BASE_URL,**args):
        self.api_url=url
        self.api_key=api_key

    def call_api(self,method,path,data):
        if method=="GET":
            result=requests.get(self.api_url+path,data)
        if method=="POST":
            result=requests.post(self.api_url+path,data)
        return Response(result)

class Response():
    def __init__(self,response):
        self.status=response.status_code
        self.encoding=response.encoding
        self.content=response.text
        self.headers=response.headers
    def extract(self):
        #try:
           return json.loads(self.content)
        #except:
            #return "Non JSON object"
