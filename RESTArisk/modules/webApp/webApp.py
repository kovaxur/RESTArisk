
from flask import Flask


class WebApp:

    class __WebApp:
        app = None
        def __init__(self):
            print("Creating app.. ")
            self.app = Flask(__name__)

    instance = None
    def __init__(self):
        if not WebApp.instance:
            WebApp.instance = WebApp.__WebApp()
    def __getinstance__(self):
        return self.instance.app


