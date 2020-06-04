#!/usr/bin/python

import getopt
import socket
import sys


class OptionsWithoutEntering(Exception):
    msg = "the options that must be entered:" \
          "\n-p : port" \
          "\n-t : protocol" \
          "\n-f : file path"

    pass


def get_opts():
    (opts, args) = getopt.getopt(sys.argv[1:], 'p:t:f:')

    if len(opts) < 3:
        raise OptionsWithoutEntering()

    fn_port = fn_protocol = fn_file_path = None
    for (option, value) in opts:
        if option == '-p':
            fn_port = int(value)
        elif option == '-t':
            fn_protocol = value
        elif option == '-f':
            fn_file_path = value

    return fn_port, fn_protocol, fn_file_path


def create_server(sv_port, sv_protocol, sv_file_path):
    data = ''
    if sv_protocol == 'tcp':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((socket.gethostname(), sv_port))
        sock.listen()
        client = sock.accept()
        data, client_addr = client[0].recv(2048), client[1]
        client[0].close()
    elif sv_protocol == 'udp':
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((socket.gethostname(), sv_port))
        data, client_addr = sock.recvfrom(2048)
        sock.close()
    else:
        print('The protocol can be "tcp" or "udp"')

    with open(sv_file_path, 'w') as file:
        file.write(data.decode('ascii'))


port, protocol, file_path = get_opts()
create_server(port, protocol, file_path)
