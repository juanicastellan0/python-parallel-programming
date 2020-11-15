#!/usr/bin/python

from socket import socket, gethostbyname, getfqdn, AF_INET, SOCK_STREAM
from getopt import getopt
from sys import argv, exit
from threading import Thread
from command_manager import manage_commands


def get_port():
    port = None
    opts, args = getopt(argv[1:], 'p:')
    if len(opts) != 1:
        print("the options that must be entered:" + "\n-p : port")
        exit(0)
    for (opt, arg) in opts:
        if opt == '-p':
            port = int(arg)

    return port


def launch_server():
    ip = gethostbyname(getfqdn())
    port = get_port()
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    print('Server launched on: ' + ip + ':' + str(port))
    sock.listen(8)
    while True:
        client_sock, client_ip = sock.accept()
        print('Client connected from ' + client_ip[0])
        thread = Thread(target=manage_commands, args=(client_sock,))
        thread.start()


launch_server()
