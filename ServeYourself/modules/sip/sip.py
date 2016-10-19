from authentication.authenticator import Authenticator
from authorization.authorization import Authorization


class SIP:
    flaskApp = None

    def __init__(self, flaskApp):
        self.flaskApp = flaskApp

        @self.flaskApp.app.route('/phone/users')
        @Authorization('admin')
        @Authenticator()
        def getSIPUsers(self):
            print("GetSIPUsers")
            return "phone-1"

        @self.flaskApp.app.route('/phone/userskszk')
        @Authorization('KSZK')
        @Authenticator()
        def getSIPUserKSZKs(self):
            print("GetSIPUsersKSZK")
            return "phone-kszk"
