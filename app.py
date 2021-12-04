from flask import Flask, render_template, request, redirect
from ping3 import ping, verbose_ping
import ping3
import sched, time, sys, os
from tqdm import tqdm


app = Flask(__name__)

@app.route("/")
def index():
        hostname='Google.com'
        delay = ping3.ping(hostname)
        delayMsLong = delay * 1000
        delayMs = round(delayMsLong, 2)
        print(hostname, delayMs, 'ms')
        return render_template('index.html', hostname=hostname, delayMs=delayMs)




def pingpong():
    while True:

        hostname='google.com'
        delay = ping3.ping(hostname)
        delayMsLong = delay * 1000
        delayMs = round(delayMsLong, 2)
        print(hostname, delayMs, 'ms')
        starttime = time.time()
        for countdown in range (15,0, -1):
            print(f"{countdown}", end="\r", flush=True)
            time.sleep(1)

if __name__ == '__main__':
    app.run()

