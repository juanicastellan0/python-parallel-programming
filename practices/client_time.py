#!/usr/bin/python

import getopt
import socket
import sys


def set_options():
    host = None
    port = 37
    protocol = 'TCP'
    opts, args = getopt.getopt(sys.argv[1:], 'h:p:t:')

    if len(opts) < 3:
        print("the options that must be entered:" + "\n-h : host" + "\n-p : port" + "\n-t : protocol")
        sys.exit(0)

    for (option, value) in opts:
        if option == '-h':
            host = value
        elif option == '-p':
            port = int(value)
        elif option == '-t':
            protocol = value if value in ['tcp', 'udp'] else 'tcp'

    return host, port, protocol


def format_date(datetime: str):
    return 'Fecha y hora actual (UTC): ' + \
           datetime.split(' ')[1] + ' ' + datetime.split(' ')[2]


def check_time():
    host, port, protoc = set_options()
    try:
        if protoc == 'tcp':
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            tcp_datetime = sock.recv(1024).decode()
            print(format_date(tcp_datetime))
        elif protoc == 'udp':
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.sendto("".encode(), (host, port))
            udp_datetime = sock.recvfrom(1024)[0].decode()
            print(format_date(udp_datetime))
    except socket.error as error:
        print(error)


check_time()
