#!/usr/bin/python
import multiprocessing
import socket
import subprocess as sp


def receiver(client):
    while True:
        client_sock, client_address = client
        command = client_sock.recv(2048).decode('ascii')
        print('Command received: ' + command)
        if command == 'exit':
            client_sock.send('Socket closed'.encode('ascii'))
            break
        with sp.Popen([command], shell=True, universal_newlines=True, stdout=sp.PIPE, stderr=sp.PIPE) as process:
            stdout, stderr = process.communicate()
            client_sock.send(('OK\n' + stdout).encode('ascii')) if process.returncode is 0 \
                else client_sock.send(('ERROR\n' + stderr).encode('ascii'))
    print('Client ' + str(client) + ' disconnected')
    client_sock.close()


def create_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostname(), 8080))
    print('Server created: ', socket.gethostname(), ':8080')
    while True:
        server.listen(5)
        client = server.accept()
        print('Connection from: ' + str(client))
        child = multiprocessing.Process(target=receiver, args=(client,))
        child.start()


create_server()
