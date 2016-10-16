
from authentication.SSO import SSO
from authentication.local import Local

class Authenticator:
    """ This class will provide a decorator to decorate calls, which must be authenticated"""

    authMethods = []
    def __init__(self):
        self.authMethods.append(SSO())
        self.authMethods.append(Local())


