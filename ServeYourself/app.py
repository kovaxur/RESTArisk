import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

import webApp
from authorization.endpoints import Endpoints as AuthorEnd
from authentication.endpoints import Endpoints as AuthenEnd
from sip.sip import SIP
from settings import Settings

class App:
    flask_app = None
    auth = None
    sip = None

    def __init__(self):
        Settings.initConfig()
        self.flask_app = webApp.WebApp()
        self.flask_app.start()

        AuthorEnd(self.flask_app)
        AuthenEnd(self.flask_app)

        self.sip = SIP(self.flask_app)

