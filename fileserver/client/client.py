#!/usr/bin/python

from socket import socket, AF_INET, SOCK_STREAM
from getopt import getopt
from sys import argv, exit


def get_options():
    host = port = None
    opts, args = getopt(argv[1:], 'h:p:')
    if len(opts) != 2:
        print("the options that must be entered:" + "\n-h : host" + "\n-p : port")
        exit(0)
    for (opt, arg) in opts:
        if opt == '-h':
            host = arg
        elif opt == '-p':
            port = int(arg)

    return host, port


def launch_client():
    host, port = get_options()
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    print('Client connected on ' + host + ':' + str(port))
    command = ''
    while command != 'exit':
        command = str(input('> '))
        sock.send(command.encode('ascii'))
        print(sock.recv(4096).decode('ascii'))


launch_client()
