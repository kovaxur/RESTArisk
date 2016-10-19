from flask import session
from flask import jsonify


class Endpoints():

    def __init__(self, role):
        self.role = role

    def __init__(self, flask_app):

        @flask_app.app.route("/roles")
        def get_role():
            return jsonify(role=session['roles'])
