class SingleTone(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if SingleTone.__instance is None:
            SingleTone.__instance = object.__new__(cls)
            cls.__init__(cls, *args, **kwargs)
        return SingleTone.__instance
