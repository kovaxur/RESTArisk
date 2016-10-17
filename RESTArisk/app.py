import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

import webApp
from authentication.authenticator import Authenticator
from sip.sip import SIP

class App:
    flaskApp = None
    auth = None
    sip = None

    def __init__(self):
        self.flaskApp = webApp.WebApp()
        self.flaskApp.start()

        self.auth = Authenticator(self.flaskApp)

        self.sip = SIP(self.flaskApp)