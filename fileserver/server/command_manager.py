import socket


def manage_commands(client: socket):
    command = client.recv(4096).decode('ascii')
    print('Command received: ' + command)
