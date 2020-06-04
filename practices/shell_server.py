#!/usr/bin/python

import socket
import subprocess as sp


def create_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostname(), 8080))
    print('Server created: ', socket.gethostname(), ':8080')
    server.listen()
    client, address = server.accept()
    while True:
        command = client.recv(2048).decode('ascii')
        if command == 'exit':
            client.send('Socket closed'.encode('ascii'))
            break
        with sp.Popen([command], shell=True, universal_newlines=True, stdout=sp.PIPE, stderr=sp.PIPE) as process:
            stdout, stderr = process.communicate()
            if process.returncode is 0:
                msg = ('OK\n' + stdout).encode('ascii')
                client.send(msg)
            else:
                msg = ('ERROR\n' + stderr).encode('ascii')
                client.send(msg)
    client.close()


create_server()
