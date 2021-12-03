import os
from ping3 import ping, verbose_ping
import ping3
import sched, time


#ping3.DEBUG = True

hostname='Google.com'

def pingpong():
    while True:

        delay = ping3.ping(hostname)
        delayMsLong = delay * 1000
        delayMs = round(delayMsLong, 2)
        print(hostname, delayMs, 'ms')
        starttime = time.time()
        time.sleep(1.0 - ((time.time() - starttime) % 60.0))

pingpong()

