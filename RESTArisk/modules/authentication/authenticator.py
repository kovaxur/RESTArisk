import datetime
from authentication.SSO import SSO
from flask import session
from flask import redirect
from settings import Settings

class Authenticator:
    """ This class will provide a decorator to decorate calls, which must be authenticated"""
    SSO = None
    def __init__(self,flask_app):
        Authenticator.SSO = SSO()

        # TODO: This disables caching, its needed for the login/logout stuff, but should be consolidated somehow,
        # to not to disable all the cahing..
        @flask_app.app.after_request
        def add_header(response):
            """
            Add headers to both force latest IE rendering engine or Chrome Frame,
            and also to cache the rendered page for 10 minutes.
            """
            response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
            response.headers['Cache-Control'] = 'public, max-age=0'
            return response

        #Starts the authentication process
        @flask_app.app.route("/auth")
        def auth():
            """
            Will do an authentication through the auth portal, if all ok, then it will redirect the user
            to the preset page, else it will show some error.
            :return:
            """
            try:
                ret = self.authenticate_force()
                if ret is True:
                    return redirect(Settings.getConfigValue("redirects","login"), code=302)
                else:
                    return redirect(ret, code=302)
            except:
                return "ERROR"

        # Returns true, if the user is authenticated, false if not, this is handy, if you wan't to do something on the
        # front-end, in case if the user is logged in.
        @flask_app.app.route("/isAuthenticated")
        def is_authenticated():
            """
            Can be checked, if the user is logged in, good for the web interface.
            :return:
            """
            try:
                if Authenticator.is_authenticated():
                    return "true"
                return "false"
            except:
                return "false"

        # Logs out the user, simply just removes the session data
        @flask_app.app.route("/logout")
        def logout():
            """
            Removes the user's session, aka logs it out.
            :return:
            """
            try:
                session.clear()
                return "true"
            except:
                return "false"

        # Returns the users' internal_id
        @flask_app.app.route("/internal_id")
        def get_internal_id():
            """
            Returns the user's internal ID
            :return:
            """
            if "internal_id" in session:
                return session["internal_id"]
            raise Exception("Error Internal Id Not Found")

        # Returns the users' name
        @flask_app.app.route("/displayName")
        def get_display_name():
            """
            Returns the user's name
            :return:
            """
            if "displayName" in session:
                return session["displayName"]
            else:
                raise Exception("Display Name Not Found")

    @classmethod
    def is_authenticated(cls):
        """
        Check whether the user is authenticated (logged in)
        :return:
        """
        # If we have the important data in the session dict
        if "access_token" in session and "refresh_token" in session and "start" in session:
            # And if those data is not null
            if session['access_token'] is not None and session['refresh_token'] is not None and session['start'] is not None:
                # And if the data is not expired..
                if (session['start'] + datetime.timedelta(seconds=session['expires_in'])) > datetime.datetime.now():
                    return True
        return False

    # Forces authentication, authenticate if you call it, won't check, if the user is already authenticated.
    @classmethod
    def authenticate_force(cls):
        """
        Forces the auth portal authentication
        :return:
        """
        return cls.SSO.authenticate()

    # Wrapper for authentication, if will act as a proxy, it will only let the command go through, if the user is
    # authenticated.
    @classmethod
    def auth(cls,func):
        """
        Authenticates a call, it checks if the user is logged in, if not, it wil throw an error.
        :param func:
        :return:
        """
        def auth_wrapper(*args,**kwargs):
            if not cls.is_authenticated():
                return redirect(Settings.getConfigValue("redirects", "error"), code=302)
            else:
                return func(args)
        return auth_wrapper