#!/usr/bin/python3

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = sys.argv[1]
port = int(sys.argv[2])


def send(sock, message):
    sock.send(message.encode('ascii'))
    code = sock.recv(1024)
    return code


while True:
    try:
        email_resp = 0
        key_resp = 0

        s.connect((host, port))
        print('Connecting...')

        msg = s.recv(1024)
        print('Message received from server: ' + msg.decode('ascii'))

        meet = 'hello|' + input('Your name: ')
        meet_resp = send(s, meet)

        if meet_resp == '200':
            email = 'email|' + input('Email: ')
            email_resp = send(s, email)

        if email_resp == '200':
            key = 'key|' + input('Key: ')
            key_resp = send(s, key)

        if key_resp == '200':
            exit_resp = send(s, 'exit')

        s.close()
        sys.exit(0)
    except socket.error:
        s.close()
        sys.exit(0)
