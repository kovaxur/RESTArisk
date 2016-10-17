import datetime
from authentication.SSO import SSO
from flask import session


class Authenticator:
    """ This class will provide a decorator to decorate calls, which must be authenticated"""
    SSO = None
    def __init__(self,flaskApp):

        self.SSO = SSO()

        #Starts the authentication process
        @flaskApp.app.route("/auth")
        def auth():
            return self.authenticateForce()

        # Returns true, if the user is authenticated, false if not, this is handy, if you wan't to do someting on the
        # front-en, in case if the user is logged in.
        @flaskApp.app.route("/isAuthenticated")
        def isAuthenticated():
            # If we have the important data in the session dict
            if "access_token" in session and "refresh_token" in session and "start" in session:
                # And if those data is not null
                if session['access_token'] is not None and session['refresh_token'] is not None and session['start'] is not None:
                    # And if the data is not expired..
                    if (session['start'] + datetime.timedelta(seconds=session['expires_in'])) > datetime.datetime.now():
                        return "true"
            return "false"

        # Logs out the user, simply just removes the session data
        @flaskApp.app.route("/logout")
        def logout():
            session.clear()
            return "LoggedOut"

        # Returns the users' internal_id
        @flaskApp.app.route("/internal_id")
        def getInternalID():
            if "internal_id" in session:
                return session["internal_id"]
            return "false"

        # Returns the users' name
        @flaskApp.app.route("/displayName")
        def getDisplayName():
            if "displayName" in session:
                return session["displayName"]
            else:
                return "false"

    # Forces authentication, authenticate if you call it, won't check, if the user is already authenticated.
    def authenticateForce(self):
        return self.SSO.authenticate()

    # Will reauthenticate if needed
    # TODO: should call authenticateForce, if the user is not authetnicated!
    def authenticate(self):
        if (session['start'] + datetime.timedelta(seconds=session['expires_in'])) < datetime.datetime.now():
            self.SSO.reauthenticate()
        return True

    # Wrapper for authentication, if will act as a proxy, it will only let the command go through, if the user is
    # authenticated.
    # TODO: the 'self' parts should be eliminated..
    @classmethod
    def auth(self,func):
        def authWrapper(*args,**kwargs):
            print(session)
            if session is None:
                return self.authenticateForce(self)
            else:
                authret = self.authenticate(self)
                if authret != True:
                    return authret
            return func(self,args)
        return authWrapper