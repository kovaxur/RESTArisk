from authentication.authenticator import Authenticator
from authorization.authorization import Authorization


class SIP:
    flaskApp = None

    def __init__(self, flaskApp):
        self.flaskApp = flaskApp

        @self.flaskApp.app.route('/phone/users')
        @Authorization.auth('admin')
        @Authenticator.auth
        def getSIPUsers(self):
            print("GetSIPUsers")
            return "phone-1"
