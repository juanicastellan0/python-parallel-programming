#!/usr/bin/python

from socket import socket, AF_INET, SOCK_STREAM
from getopt import getopt
from sys import argv, exit


def get_options():
    host = port = text = hash_func = None
    opts, args = getopt(argv[1:], 'a:c:h:p:')
    if len(opts) != 4:
        print("the options that must be entered:" + "\n-a : host" + "\n-p : port"
              + "\n-h : hash function" + "\n-c : text")
        exit(0)
    for (opt, arg) in opts:
        if opt == '-a':
            host = arg
        elif opt == '-p':
            port = int(arg)
        elif opt == '-h':
            hash_func = arg
        elif opt == '-c':
            text = arg

    return host, port, hash_func, text


def launch_client():
    host, port, hash_func, text = get_options()
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    print('Connected on ' + host + ':' + str(port))
    sock.send(hash_func.encode())
    response_code = sock.recv(1024).decode()
    print(response_code)
    if int(response_code) == 404:
        print('Incorrect hash function')
        exit(0)
    else:
        sock.send(text.encode())
        hashed_text = sock.recv(1024).decode()
        print(hash_func + ' for ' + text + ': ' + hashed_text)
        exit(0)


launch_client()
