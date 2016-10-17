import requests
from requests.auth import HTTPBasicAuth
import datetime

from .authentication import Authentication
from flask import redirect
from flask import request
from flask import session
import hashlib
import json

class SSO(Authentication):
    hostname = "https://auth.sch.bme.hu/"
    username = ""
    password = ""
    scope = "basic"
    _tokens = None
    redirectOnAuth = "index.html"

    def __init__(self):
        pass

    def reauthenticate(self):
        data = {}
        data['grant_type'] = 'refresh_token'
        data['refresh_token'] = session['refresh_token']
        ch = self.curlExec("oauth2/token", data)
        print(ch.text)
        self.sessionCreate(ch)


    def authenticate(self):
        data = {}
        print("auth1")
        if request.args.get('code') is None:
            print("auth2")
            data['grant_type']      = "client_credentials"
            data['access_token']    = self.curlExec("oauth2/token",data).json()['access_token']
            print("auth3")
            res = self.curlExec("oauth2/resource", data)
            if res.status_code == 200:
                print("auth4")
                userHash = str(hashlib.sha1(str(request.remote_addr).encode('utf-8') + str(request.headers.get('User-Agent')).encode('utf-8')).hexdigest())
                URL = self.hostname + "site/login?response_type=code&client_id=" + self.username + "&state=" + userHash + "&scope=" + self.scope
                return redirect(URL, code=302)
            print("auth5")
        else:
            data['grant_type'] = "authorization_code"
            data['code'] = request.args.get('code')
            ch = self.curlExec("oauth2/token",data)
            self.sessionCreate(ch)
            return redirect(self.redirectOnAuth,code=302)


    def curlExec(self,urlPart, data):
        if urlPart != "oauth2/resource":
            ret = requests.post(self.hostname + urlPart,data,auth=HTTPBasicAuth(self.username,self.password))
            return ret
        else:
            ret = requests.post(self.hostname + urlPart, data)
            return ret

    def sessionCreate(self,ch):
        data = json.loads(ch.text)
        session['access_token']     = data['access_token']
        session['refresh_token']    = data['refresh_token']
        session['token_type']       = data['token_type']
        session['scope']            = data['scope']
        session['expires_in']       = 10
        session['start']            = datetime.datetime.now()


if __name__ == "__main__":
    s = SSO()
    s.authenticate()



