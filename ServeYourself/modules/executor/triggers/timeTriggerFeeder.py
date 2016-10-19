import threading
import time

from libs.signals import signals
from libs.tools import singleton


class TimeTriggerFeeder(threading.Thread, singleton.Singleton):
    tick = signals.time_tick

    def __init__(self, tick_time=60):
        super(TimeTriggerFeeder, self).__init__()
        self._tick_time = tick_time
        self._name = "TimeTriggerFeeder"
        self._running = True

    def __repr__(self):
        return self.name

    @property
    def name(self):
        return self._name

    def stop(self):
        self._running = False

    def run(self):
        while self._running:
            if (int(time.time()) % self._tick_time) == 0:
                self.tick.send(self)
            time.sleep(1)

if __name__ == "__main__":
    def subscriber(data):
        print("Got a signal sent by %r" % data.name)

    print('TimeTriggerFeeder test start.')
    s = signals.time_tick
    s.connect(subscriber)
    trigger = TimeTriggerFeeder.instance(1)
    trigger.start()
    time.sleep(5)
    trigger.stop()
    print('TimeTriggerFeeder test start.')
