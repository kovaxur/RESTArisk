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


    def authenticateForce(self):
        return self.SSO.authenticate()

    def authenticate(self):
        if (session['start'] + datetime.timedelta(seconds=session['expires_in'])) < datetime.datetime.now():
            self.SSO.reauthenticate()
            #return self.authenticateForce(self)
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