from authentication.authenticator import Authenticator
from authorization.authorization import Authorization
from module.endpoints import BaseEndpoints
from flask import jsonify
from settings import Settings
from voip.asterisk_sip import AsteriskSIP


class Asterisk(BaseEndpoints):
    def __init__(self, flask_app):
        self.flask_app = flask_app

        self.sip = AsteriskSIP()

        @self.flask_app.app.route('/voip/asterisk/phones')
        @Authenticator()
        def get_sip_peers(cls):
            """ This will return the current user's sip peers """
            return jsonify(sippeers=self.sip.get_sip_peers())

        @self.flask_app.app.route('/phone/userskszk')
        @Authorization('KSZK')
        @Authenticator()
        def getSIPUserKSZKs(self):
            print("GetSIPUsersKSZK")
            return "phone-kszk"

    def get_sip_peers(self):
        return ['one', 'two']