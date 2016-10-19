from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    def __init__(self, name: str):
        self._name = name

    def __repr__(self):
        return self.name

    @staticmethod
    def factory(type: str, *args, **kwargs):
        """Factory pattern method"""
        if type == 'PrintAction':
            return PrintAction(*args, **kwargs)

        assert 0, "Bad action type creation: " + type

    @staticmethod
    def get_types() -> list:
        """
        :return:
         supported trigger types
        """
        return ['PrintAction']

    @property
    def name(self):
        return self._name

    @abstractmethod
    def execute(self) -> bool:
        """
        :return:
         True: action successfully completed
         Fasle: aborted
        """
        return False

    @abstractmethod
    def cancel(self):
        pass


class PrintAction(Base):
    def __init__(self, name: str, msg: str):
        super(PrintAction, self).__init__(name)
        self._msg = msg

    def execute(self):
        print(self._msg)
        return True

    def cancel(self):
        pass

if __name__ == "__main__":
    action = Base.factory('PrintAction', 'Test action', 'Test msg')
    action.execute()
