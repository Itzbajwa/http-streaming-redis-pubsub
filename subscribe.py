#!/usr/bin/env python

import gevent.monkey
gevent.monkey.patch_all()

import sys
import requests
import gevent
import gevent.pool
import random
import json

def consume(id):
    r = requests.get('http://127.0.0.1:5000/stream/' + str(id), stream=True)
    for line in r.iter_lines(10):
        try:
            obj = json.loads(line)
        except:
            print line
            raise

        if random.randint(0, 99) <= 1:
            print obj


POOL_SIZE = 1000

if __name__ == '__main__':

    pool = gevent.pool.Pool(POOL_SIZE)
    greenlets = pool.map(consume, xrange(POOL_SIZE))
    gevent.joinall(greenlets)

