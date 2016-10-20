import threading


class Singleton(object):
    __singleton_lock = threading.Lock()
    __singleton_instance = None

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls(*args, **kwargs)
        return cls.__singleton_instance
