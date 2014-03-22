#!/usr/bin/env python

import gevent.monkey
gevent.monkey.patch_all()

import redis
import flask
from gevent.pywsgi import WSGIServer
import gevent.pool

import json

red = redis.StrictRedis()

app = flask.Flask(__name__)

@app.route('/stream/<int:id>')
def stream(id):
    pbsb = red.pubsub()
    pbsb.subscribe('time')

    def generate():
        for item in pbsb.listen():
            if item['type'] == 'message':
                obj = json.loads(item['data'])
                obj['stream'] = id
                yield json.dumps(obj) + '\n'

    return flask.Response(generate())

if __name__=='__main__':
    pool = gevent.pool.Pool(10000)
    http_server = WSGIServer(('', 5000), app, spawn=pool)
    http_server.serve_forever()
