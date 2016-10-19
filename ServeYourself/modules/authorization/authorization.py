from authorization.authordb import AuthDB


class Authorization:
    def __init__(self):
        pass

    @classmethod
    def auth(cls, func):
        def auth_wrapper(*args, **kwargs):
            return func(args, kwargs)
        return auth_wrapper
