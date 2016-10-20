from flask import redirect
from flask import session
from settings import Settings
from functools import wraps


class Authorization(object):

    def __init__(self, role_needed):
        self.role_needed = role_needed

    def __call__(self, f):
        @wraps(f)
        def auth_wrapper(*args):
            try:
                user_role = session['roles']
            except:
                return redirect(Settings.getConfigValue("redirects", "error"), code=302)
            if self.role_needed in user_role:
                return f(args)
            else:
                return redirect(Settings.getConfigValue("redirects", "error"), code=302)
        return auth_wrapper
