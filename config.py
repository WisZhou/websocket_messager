#coding=utf-8

import logging

#============project config============
LOG_LEVEL = logging.DEBUG
#WEBSOCKET
WEBSOCKET_HOST = '127.0.0.1' # The host Client(Browser) access
MESSAGER_HOST = '127.0.0.1' # The host server access
WEBSOCKET_PORT = 8100 # The service listened port
WEBSOCKET_URL = 'ws://%s:%s/ws' % (WEBSOCKET_HOST, WEBSOCKET_PORT)
MESSAGER_URL = 'http://%s:%s/msg' % (MESSAGER_HOST, WEBSOCKET_PORT)
#================project config end===============
