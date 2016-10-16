
from flask import Flask
from threading import Thread
from flask import request
from flask import send_from_directory
import os

class WebApp(Thread):
    app = None
    def __init__(self):
        self.app = Flask(__name__)
        super(WebApp, self).__init__()

    def run(self):

        @self.app.route('/<path:path>')
        def sendStatic(path):
            print(path)
            return send_from_directory('../../static', path)

        self.app.run(host='0.0.0.0', port=5000, debug=False)

    def stop(self):
        try:
            func = request.environ.get('werkzeug.server.shutdown')
            if func is None:
                raise RuntimeError('Not running with the Werkzeug Server')
            func()
        except:
            pass



