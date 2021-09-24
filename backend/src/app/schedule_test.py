import sched
import datetime
import threading
import time

def hello():
    print('hello')

s = sched.scheduler(time.time)

str_t = '2021-09-23T19:20:00.000+09:00'
t = datetime.datetime.fromisoformat(str_t).timestamp()

print(t)
s.enterabs(t,1,hello)

s.run()
