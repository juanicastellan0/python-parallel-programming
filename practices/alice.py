#!/usr/bin/python

from sys import exit
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, getfqdn


def connect():
    alice_sock = socket(AF_INET, SOCK_STREAM)
    alice_sock.bind(('', 8080))
    ip = gethostbyname(getfqdn())
    print('Alice connected at ' + ip + ' on port 8080 and is waiting for Bob')
    alice_sock.listen(1)
    bob_sock, bob_ip = alice_sock.accept()
    print('Bob connected at ' + bob_ip[0])

    return alice_sock, bob_sock


def get_message(bob_sock: socket):
    while True:
        message = bob_sock.recv(1024).decode()
        if message == 'cambio':
            break
        elif message == 'exit':
            print('Connection finished')
            exit(0)
        print('- Bob: ' + message)


def send_message(bob_sock: socket):
    while True:
        message = input('- Alice: ').encode()
        bob_sock.send(message)
        if message.decode() == 'cambio':
            break
        elif message.decode() == 'exit':
            exit(0)


def start_walkie_talkie():
    alice_sock, bob_sock = connect()
    while True:
        get_message(bob_sock)
        send_message(bob_sock)


start_walkie_talkie()
