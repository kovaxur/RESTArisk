from libs.actions import action
from libs.triggers import trigger
import threading
from libs.signals import signals


class Base(threading.Thread):
    def __init__(self, name: str, trig: trigger.Base, act: action.Base):
        super(Base, self).__init__()
        self._name = name
        self._trigger = trig
        self._action = act
        self._trigger_signal = trig.raising_signal
        self._ready_signal = signals.task_is_ready

        def ready_handler(sender,*args, **kwargs):
            self._ready_signal.send(self)
        self.ready_handler = ready_handler
        self._trigger_signal.connect(ready_handler, sender=self._trigger)

    @staticmethod
    def factory(type: str, name: str, *args, **kwargs):
        """Factory pattern method"""
        if type == 'Base':
            return Base(name, *args, **kwargs)
        if type == 'PrintTask':
            # Trigger:
            if 'deltat' in kwargs:
                trig = trigger.Base.factory('Time-delay-once', deltat=kwargs['deltat'])
            elif 'at' in kwargs:
                trig = trigger.Base.factory('Time-at-once', at=kwargs['at'])
            else:
                trig = None
                # TODO: exception

            # Action:
            if 'msg' not in kwargs:
                pass
                # TODO: exception

            act = action.Base.factory('PrintAction', 'Printer', msg=kwargs['msg'])

            return Base(name, trig, act)

        assert 0, "Bad task type creation: " + type + "valid: " + str(Base.get_types())

    @staticmethod
    def get_types():
        """Return the supported trigger types"""
        return ['Base', 'PrintTask']

    def __repr__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def trigger(self):
        return self._trigger

    @trigger.setter
    def trigger(self, value):
        self._trigger = value

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value

    def run(self):
        """Don't call it. It's for threading"""
        if self._action.execute():
            signals.successfully_completed.send(self)
            return True
        else:
            signals.failed.send(self)
            return False

    def repeatable(self):
        return self.trigger.repeatable

    def cancel(self):
        self._action.cancel()

    def execute(self):
        """Alias for start()"""
        return self.start()

    @property
    def ready(self):
        """Return the signal which will be fire"""
        return self._ready_signal

if __name__ == "__main__":
    import time
    from libs.triggers import timeTriggerFeeder


    def executor(task: Base):
        print("Got a signal sent by %r" % task.name)
        task.execute()


    timeTriggerFeeder.TimeTriggerFeeder.instance(1).start()

    print('Task test start.')

    task1 = Base.factory('PrintTask', 'task1', deltat=3, msg='Message1')
    task1.ready.connect(executor)
    task2 = Base.factory('PrintTask', 'task2', deltat=6, msg='Message2')
    task2.ready.connect(executor)

    time.sleep(10)
    timeTriggerFeeder.TimeTriggerFeeder.instance().stop()
    print('Task test stop.')
