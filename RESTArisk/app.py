import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

import webApp


class App:
    flaskApp = None

    def __init__(self):
        self.flaskApp = webApp.WebApp().__getInstance__()
        self.flaskApp.run(host="0.0.0.0",port=5000)



