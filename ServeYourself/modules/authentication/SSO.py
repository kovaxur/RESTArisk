import requests
from requests.auth import HTTPBasicAuth
import datetime
from flask import request
from flask import session
import hashlib
import json
from settings import Settings
from .authentication import Authentication

"""This class does the authentication through an SSO server(oauth2)"""
class SSO(Authentication):
    hostname = None
    username = None
    password = None
    scope = "basic+displayName+admembership"
    _tokens = None

    def __init__(self):
        self.hostname = Settings.getConfigValue("oauth2","hostname")
        self.username = Settings.getConfigValue("oauth2","username")
        self.password = Settings.getConfigValue("oauth2","password")

    # This will do a reauthenticate, if the users' session expires.
    def reauthenticate(self):
        data = {'grant_type':'refresh_token','refresh_token':session['refresh_token']}
        ch = self.curl_exec("oauth2/token", data)
        self.set_session_data()
        self.session_create(ch)

    # This will do the authentication
    def authenticate(self):
        data = {}
        # If we are redirected from the SSO site, or not
        if request.args.get('code') is None:
            # First we need a token for our app
            data['grant_type'] = "client_credentials"
            access_token = self.curl_exec("oauth2/token", data).json()['access_token']
            data['access_token'] = access_token
            res = self.curl_exec("oauth2/resource", data)
            # If we have our token, we will ask for the user's access_code (this will throw the user to the login page)
            if res.status_code == 200:
                # Hash some data about the user
                user_hash = str(hashlib.sha1(str(request.remote_addr).encode('utf-8') + str(request.headers.get('User-Agent')).encode('utf-8')).hexdigest())
                # Get the REST API's url
                url = self.hostname + "site/login?response_type=code&client_id=" + self.username + "&state=" + user_hash + "&scope=" + self.scope
                # Redirect the user to the login page
                return url
            else:
                # If something bad happens, some error page should be shown.
                raise Exception("Login Error")
        else:
            # If we have the access code, get the user's access token
            data['grant_type'] = "authorization_code"
            data['code'] = request.args.get('code')
            ch = self.curl_exec("oauth2/token", data)
            if ch.status_code == 200:
                # If we have the access_token, create the user's session, and get the user's data
                self.session_create(ch)
                self.set_session_data()
                # Finally redirect the user to the home page
                return True
            else:
                # Otherwise redirect to an error page
                raise Exception("Login Error")

    # Just a simple requests.post wrapper
    def curl_exec(self, urlPart, data):
        if urlPart != "oauth2/resource":
            ret = requests.post(self.hostname + urlPart,data,auth=HTTPBasicAuth(self.username,self.password))
            return ret
        else:
            ret = requests.post(self.hostname + urlPart, data)
            return ret

    # This creates the user session from the data got from the SSO server.
    def session_create(self, ch):
        data = json.loads(ch.text)
        session['access_token'] = data['access_token']
        session['refresh_token'] = data['refresh_token']
        session['token_type'] = data['token_type']
        session['scope'] = data['scope']
        session['expires_in'] = data['expires_in']
        session['start'] = datetime.datetime.now()

    # This adds some additional data to the user session
    def set_session_data(self):
        data = self.get_data()
        session['internal_id'] = data['internal_id']
        session['displayName'] = data['displayName']
        session['roles'] = data["admembership"]

    # This asks for additional data about the user, such as username, the user's name, email etc..
    def get_data(self):
        url = self.hostname + "api/profile/?access_token=" + session['access_token']
        ret = requests.get(url)
        if ret is not None and ret.status_code == 200:
            data = ret.json()
            if data is not None:
                return data
        return None




