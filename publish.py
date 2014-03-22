#!/usr/bin/env python

import redis
import datetime
import time
import json

r = redis.StrictRedis()

# Need to look at redis output buffer limits for throttling slow connections

def publish():
    t = datetime.datetime.now().isoformat()
    msg = json.dumps({'time': t})
    print msg
    r.publish('time', msg)

if __name__=='__main__':
    while True:
        publish()
	time.sleep(1)

