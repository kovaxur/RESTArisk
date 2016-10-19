import datetime
from authentication.SSO import SSO
from flask import session
from flask import redirect
from settings import Settings
from functools import wraps


class Authenticator:
    """ This class will provide a decorator to decorate calls, which must be authenticated"""
    SSO = None

    def __init__(self):
        Authenticator.SSO = SSO()

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
    def authenticate_force(self):
        """
        Forces the auth portal authentication
        :return:
        """
        return self.SSO.authenticate()

    # Wrapper for authentication, if will act as a proxy, it will only let the command go through, if the user is
    # authenticated.
    def __call__(self, func):
        """
        Authenticates a call, it checks if the user is logged in, if not, it wil throw an error.
        :param func:
        :return:
        """
        @wraps(func)
        def auth_wrapper(*args):
            if not self.is_authenticated():
                return redirect(Settings.getConfigValue("redirects", "error"), code=302)
            else:
                return func(args)
        return auth_wrapper
