from blinker import signal
from blinker import Signal

time_tick = signal('TIME-TICK')
time = signal('TIME')
any = signal(Signal.ANY)
time_default = signal('TIME-DEFAULT')
delete_me = signal('DELETE-ME')
successfully_completed = signal('SUCCESSFULLY-COMPLETED')
failed = signal('FAILED')
task_is_ready = signal('TASK-IS-READY')
