from eventlet import wsgi, patcher
patcher.monkey_patch()
import sys, getopt, eventlet
from cmp.wsgi import application

addr, port = '0.0.0.0', 8080
opts, _ = getopt.getopt(sys.argv[1:], "b:")
for opt, value in opts:
    if opt == '-b':
        addr,port = value.split(":")

wsgi.server(eventlet.listen((addr, int(port))), application)