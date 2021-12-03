from ping3 import ping, verbose_ping
import ping3
import sched, time, sys, os
from tqdm import tqdm


#ping3.DEBUG = True

hostname='Google.com'

def pingpong():
    while True:

        delay = ping3.ping(hostname)
        delayMsLong = delay * 1000
        delayMs = round(delayMsLong, 2)
        print(hostname, delayMs, 'ms')
        starttime = time.time()
        for countdown in range (15,0, -1):
            print(f"{countdown}", end="\r", flush=True)
            time.sleep(1)

pingpong()

