
from flask import Flask
from threading import Thread
from flask import request
from flask import send_from_directory


class WebApp(Thread):
    app = None
    session = None
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
        super(WebApp, self).__init__()

    def run(self):

        @self.app.route('/<path:path>')
        def sendStatic(path):
            return send_from_directory('../../static', path)


        self.app.run(host='0.0.0.0', port=5000, debug=False,threaded=True)

    def stop(self):
        try:
            func = request.environ.get('werkzeug.server.shutdown')
            if func is None:
                raise RuntimeError('Not running with the Werkzeug Server')
            func()
        except:
            pass



