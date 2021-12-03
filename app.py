import os
from ping3 import ping, verbose_ping
import ping3

#ping3.DEBUG = True

hostname='cammit.co'

def pingpong():
    delay = ping3.ping(hostname)
    delayMs = delay * 1000
    print(hostname, delayMs, 'ms')

pingpong()

