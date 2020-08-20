#!/usr/bin/python
import getopt
import multiprocessing
import socket
import sys


def set_port():
    opts, args = getopt.getopt(sys.argv[1:], 'p:')

    if len(opts) != 1:
        print("the option that must be entered:" + "\n-p : port")

    return int(opts[0][1])


def reply_to_client(client: socket, host):
    while True:
        msg = client.recv(2048).decode()
        inverted_msg = '--> ' + msg[::-1]
        client.send(inverted_msg.encode())


def init_server():
    port = set_port()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))

    while True:
        sock.listen(16)
        client, host = sock.accept()

        process = multiprocessing.Process(target=reply_to_client, args=(client, host))
        process.start()


init_server()
