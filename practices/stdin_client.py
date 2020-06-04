#!/usr/bin/python

import getopt
import socket
import sys


class OptionsWithoutEntering(Exception):
    msg = "the options that must be entered:" \
          "\n-a : address" \
          "\n-p : port" \
          "\n-t : protocol"

    pass


def get_options():
    (opts, args) = getopt.getopt(sys.argv[1:], 'a:p:t:')

    if len(opts) != 3:
        raise OptionsWithoutEntering()

    fn_addr = fn_port = fn_protocol = None
    for (option, value) in opts:
        if option == '-a':
            fn_addr = value
        elif option == '-p':
            fn_port = int(value)
        elif option == '-t':
            fn_protocol = value

    return fn_addr, fn_port, fn_protocol


def get_stdin():
    stdin = ''
    for line in sys.stdin:
        stdin += line

    return stdin


def create_client(sv_address, sv_port, cli_protocol):
    if cli_protocol == 'tcp':
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((sv_address, sv_port))
        print('Connecting to', sv_address, ':', sv_port)
        print("Type something, then press Ctrl+D when you're done")
        stdin = get_stdin()
        client.send(stdin.encode('ascii'))
    elif cli_protocol == 'udp':
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Start typing and press CTRL-D when you're done")
        stdin = get_stdin()
        s.sendto(stdin.encode('ascii'), (sv_address, sv_port))


address, port, protocol = get_options()
create_client(address, port, protocol)
