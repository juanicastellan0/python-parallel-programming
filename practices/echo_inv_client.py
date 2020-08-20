#!/usr/bin/python

import getopt
import sys
import socket


def set_options():
    host = port = None
    opts, args = getopt.getopt(sys.argv[1:], 'h:p:')

    if len(opts) < 2:
        print("the options that must be entered:" + "\n-h : host" + "\n-p : port")
        sys.exit(0)

    for (opt, value) in opts:
        if opt == '-h':
            host = value
        elif opt == '-p':
            port = int(value)

    return host, port


def init_client():
    host, port = set_options()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    while True:
        msg = str(input('>>> '))
        sock.send(msg.encode())
        ans = sock.recv(4069).decode()
        print(ans)


init_client()
