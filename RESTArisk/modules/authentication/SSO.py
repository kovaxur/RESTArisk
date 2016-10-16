import requests
from requests.auth import HTTPBasicAuth

from .authentication import Authentication


class SSO(Authentication):
    hostname = "https://auth.sch.bme.hu/"
    username = ""
    password = ""
    scope = None
    _tokens = None

    def __init__(self):
        pass

    def authenticate(self,userToken):
        data = {'grant_type':'client_credentials'}
        data['access_token'] = self.curlExec("oauth2/token",data).json()['access_token']


        print(self.curlExec("oauth2/resource",data).text)


    def curlExec(self,urlPart, data):
        if urlPart != "oauth2/resource":
            ret = requests.post(self.hostname + urlPart,data,auth=HTTPBasicAuth(self.username,self.password))
            return ret
        else:
            ret = requests.post(self.hostname + urlPart, data)
            return ret




if __name__ == "__main__":
    s = SSO()
    s.authenticate()



