import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

import webApp
from authentication.authenticator import Authenticator
from sip.sip import SIP
from settings import Settings

class App:
    flaskApp = None
    auth = None
    sip = None

    def __init__(self):
        Settings.initConfig()
        self.flaskApp = webApp.WebApp()
        self.flaskApp.start()

        self.auth = Authenticator(self.flaskApp)

        self.sip = SIP(self.flaskApp)

