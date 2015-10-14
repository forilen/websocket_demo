# coding: utf-8

import os
from urlparse import parse_qs

from oslo.config import cfg
from gevent import select
import redis
import time
try:
    import uwsgi
except ImportError:
    uwsgi = None


def application(env, start_response):
    # complete the handshake
    uwsgi.websocket_handshake(env['HTTP_SEC_WEBSOCKET_KEY'],
                              env.get('HTTP_ORIGIN', ''))
    parse = parse_qs(env['QUERY_STRING'])
    print("parse")
    counter = 0
    while True:
        # msg = uwsgi.websocket_recv()
        uwsgi.websocket_send("msg %d" % counter)
        counter += 1
        time.sleep(5)
