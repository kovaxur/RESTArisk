import datetime
from authentication.SSO import SSO
from flask import session


class Authenticator:
    """ This class will provide a decorator to decorate calls, which must be authenticated"""
    SSO = None
    def __init__(self,flaskApp):
        self.SSO = SSO()

        @flaskApp.app.route("/auth")
        def auth():
            return self.authenticateForce()

        @flaskApp.app.route("/isAuthenticated")
        def isAuthenticated():
            if "access_token" in session and "refresh_token" in session and "start" in session:
                if session['access_token'] != None and session['refresh_token'] != None and session['start'] != None:
                    if (session['start'] + datetime.timedelta(seconds=session['expires_in'])) > datetime.datetime.now():
                        return True
            return False

        @flaskApp.app.route("/logout")
        def logout():
            session.clear()
            return "LoggedOut"


    def authenticateForce(self):
        return self.SSO.authenticate()

    def authenticate(self):
        if (session['start'] + datetime.timedelta(seconds=session['expires_in'])) < datetime.datetime.now():
            self.SSO.reauthenticate()
        return True

    @classmethod
    def auth(self,func):
        def authWrapper(*args,**kwargs):
            print(session)
            if session is None:
                print("auth needed")
                return self.authenticateForce(self)
            else:
                authret = self.authenticate(self)
                if authret != True:
                    return authret
            return func(self,args)

        return authWrapper