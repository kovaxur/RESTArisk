import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

import webApp
from authentication.authenticator import Authenticator


class App:
    flaskApp = None

    def __init__(self):
        self.flaskApp = webApp.WebApp()
        self.flaskApp.start()

        time.sleep(5)
        #self.flaskApp.run(host="0.0.0.0",port=5000)
        self.flaskApp.stop()

        print("lofasy")
        #auth = Authenticator()
        #auth.authenticate("mytoken")


