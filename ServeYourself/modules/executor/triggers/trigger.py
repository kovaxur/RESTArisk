from abc import ABCMeta, abstractmethod
from datetime import datetime
from datetime import timedelta
from libs.signals import signals


class Base(metaclass=ABCMeta):
    def __init__(self,
                 name: str,
                 repeatable: bool = False,
                 subscriber_signal: signals.signal = None,
                 raising_signal: signals.signal = None):
        self._name = name
        self._repeatable = repeatable
        self._subscriber_signal = subscriber_signal
        self._raising_signal = raising_signal

        @self._subscriber_signal.connect
        def event_handler(sender, **kwargs):
            """It's need to subscribe to an event"""
            self.event(sender, **kwargs)

        self.event_handler = event_handler

    @staticmethod
    def factory(type, name='', *args, **kwargs):
        """Factory pattern method"""
        if type == 'Time':
            return Time(name, *args, **kwargs)
        if type == 'Time-at-once':
            return Time('Time-at-once', datetime.now(kwargs['at']))
        if type == 'Time-delay-once':
            return Time('Time-delay-once', datetime.now() + timedelta(seconds=kwargs['deltat']))

        assert 0, "Bad trigger type creation: " + type

    @staticmethod
    def get_types():
        """Return the supported trigger types"""
        return ['Time', 'Time-at-onetime', 'Time-delay-onetime']

    @abstractmethod
    def event(self, sender, **kwargs):
        """This method will be called if some event occurred
        It will maintain the conditions"""
        pass

    @abstractmethod
    def end(self):
        pass

    def fire(self):
        """Send signal"""
        self._raising_signal.send(self)
        self.end()

    @property
    def repeatable(self):
        """
        Return:
        True: repeatable
        False: not repeatable
        """
        return self._repeatable

    @property
    def name(self):
        """Return name of the trigger"""
        return self._name

    @property
    def raising_signal(self):
        """Return the signal which will be fire"""
        return self._raising_signal

    def __repr__(self):
        return self.name


class Time(Base):
    def __init__(self, name, trigger_time, repeatable=False):
        super(Time, self).__init__(name, repeatable, signals.time_tick, signals.time_default)
        self._trigger_time = trigger_time

    def event(self, sender, **kwargs):
        if self._trigger_time <= datetime.now():
            self.fire()

    def end(self):
        self._trigger_time = datetime.now() + timedelta(weeks=10)


if __name__ == "__main__":
    import time
    import pprint
    from libs.triggers import timeTriggerFeeder


    def subscriber(data):
        print("Got a signal sent by %r" % data.name)

    print('Trigger test start.')
    time_trigger = timeTriggerFeeder.TimeTriggerFeeder.instance(1)
    time_trigger.start()
    t = Base.factory('Time', 'TRIGGER TEST', datetime.now() + timedelta(seconds=7))
    s = signals.time_default
    s.connect(subscriber)
    time.sleep(10)
    time_trigger.stop()
    try:
        t = Base.factory('NOT EXISTENT TASK NAME', 'time', datetime.now() + timedelta(seconds=7))
    except AssertionError as e:
        print(e)

    pprint.pprint("exist ones: ")
    pprint.pprint(Base.get_types())

    print('Trigger test stop.')
