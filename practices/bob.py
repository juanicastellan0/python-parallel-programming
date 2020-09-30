#!/usr/bin/python

from sys import exit, argv
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, getfqdn
from getopt import getopt


def connect():
    opts, args = getopt(argv[1:], 'i:')
    alice_ip = opts[0][1] if opts else ''
    bob_sock = socket(AF_INET, SOCK_STREAM)
    bob_sock.connect((alice_ip, 8080))
    print('Bob connected with Alice')

    return bob_sock


def get_message(bob_sock):
    while True:
        message = bob_sock.recv(1024).decode()
        if message == 'cambio':
            break
        elif message == 'exit':
            print('Connection finished')
            exit(0)
        print('- Alice: ' + message)


def send_message(bob_sock: socket):
    while True:
        message = input('- Bob: ').encode()
        bob_sock.send(message)
        if message.decode() == 'cambio':
            break
        elif message.decode() == 'exit':
            exit(0)


def start_walkie_talkie():
    bob_sock = connect()
    while True:
        send_message(bob_sock)
        get_message(bob_sock)


start_walkie_talkie()
