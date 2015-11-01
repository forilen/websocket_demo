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


def prepare_redis():
    rd = redis.Redis(
        host="127.0.0.1",
        port=6379)
    print('Connecting to redis on ("%s", %s)',
             "127.0.0.1",
             "6379")
    return rd
rd = prepare_redis()


def application(env, start_response):
    parse = parse_qs(env['QUERY_STRING'])
    if 'uid' not in parse:
        print('Connection error: uid not found')
        return ''
    uid = parse['uid'][0]

    uwsgi.websocket_handshake(env['HTTP_SEC_WEBSOCKET_KEY'],
                              env.get('HTTP_ORIGIN', ''))
    print('Connection to websocket %s', uid)

    channel = rd.pubsub()
    channel.subscribe(uid)
    print('Subscribe to channel %s', uid)
    ws_fd = uwsgi.connection_fd()
    rd_fd = channel.connection._sock.fileno()

    while True:
        # wait max 4 seconds to allow ping to be sent
        ready = select.select([ws_fd, rd_fd], [], [], 4.0)
        # send ping on timeout
        if not ready[0]:
            uwsgi.websocket_recv_nb()
        for fd in ready[0]:
            if fd == ws_fd:
                try:
                    msg = uwsgi.websocket_recv_nb()
                    if msg:
                        print('Pub msg %s', msg)
                        rd.publish(uid, msg)
                except IOError:
                    print('Websocket Closed: %s', uid)
                    return ''
            elif fd == rd_fd:
                msg = channel.parse_response()
                # only interested in user messages
                if msg[0] == 'message':
                    print('Send msg %s', msg[2])
                    uwsgi.websocket_send(msg[2])
