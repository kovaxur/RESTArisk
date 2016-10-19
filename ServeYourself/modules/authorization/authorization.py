from flask import redirect
from flask import session
from flask import jsonify

from settings import Settings


class Authorization(object):

    def __init__(self, flask_app):

        @flask_app.app.route("/role")
        def get_role():
            return jsonify(role=session['role'])

    @classmethod
    def auth(cls, role):

        def arg_wrapper(f):
            def auth_wrapper(*args, **kwargs):
                try:
                    user_role = session['role']
                except:
                    return redirect(Settings.getConfigValue("redirects", "error"), code=302)
                if user_role == role:
                    return f(args, kwargs)
                else:
                    return redirect(Settings.getConfigValue("redirects", "error"), code=302)
            return auth_wrapper
        return arg_wrapper
