from authentication.authenticator import Authenticator

class SIP:
    flaskApp = None
    def __init__(self,flaskApp):
        self.flaskApp = flaskApp

        @self.flaskApp.app.route('/phone/users')
        @Authenticator.auth
        def getSIPUsers(self,username):
            print("GetSIPUsers")
            return "phone-1"