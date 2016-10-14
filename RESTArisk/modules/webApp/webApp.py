
from flask import Flask


class WebApp:

    class __WebApp:
        def __init__(self):
            pass


    instance = None
    def __init__(self):
        if not WebApp.instance:
            WebApp.instance = WebApp.__WebApp()
    def __getinstance__(self):
        return self.instance

