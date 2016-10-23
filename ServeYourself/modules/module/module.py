

class BaseModule:
    """ This is the base class for the module's main class, please inherit from this """

    def __init__(self, flask_app):
        self.flask_app = flask_app
