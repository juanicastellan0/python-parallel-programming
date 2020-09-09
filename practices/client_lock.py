#!/usr/bin/python

import socket
import getopt
import sys
from multiprocessing import Lock, Process

COMMANDS = ["ABRIR", "AGREGAR", "LEER", "CERRAR"]


def set_port():
    opts, args = getopt.getopt(sys.argv[1:], 'p:')

    return int(opts[0][1])


def init_client(lock, client, address):
    file_name = file = None
    client.send(('Server commands are ' + str(COMMANDS) + '\n').encode())

    while True:
        command = client.recv(256).decode()
        command = command.upper().strip()
        if command == 'ABRIR':
            if file is not None:
                client.send('The file is already open\n'.encode())
                continue
            client.send('Enter the file name: '.encode())
            file_name = client.recv(256).decode()
            file = open(file_name, 'a')
            client.send('The file was opened\n'.encode())
        elif command == 'AGREGAR':
            if file is None:
                client.send('A file must be opened first\n'.encode())
                continue
            client.send('Write something to add to the file:\n'.encode())
            user_string = client.recv(256).decode()
            lock.acquire()
            file.writelines(user_string)
            file.flush()
            lock.release()
            client.send('The file has been written\n'.encode())
        elif command == 'LEER':
            if file is None:
                client.send('A file must be opened first\n'.encode())
                continue
            with open(file_name, 'r') as read_fd:
                content = str(read_fd.read()) + '\n'
                client.send(content.encode())
        elif command == 'CERRAR':
            client.send('Closing the file\n'.encode())
            if file is not None:
                file.close()
            break
        else:
            client.send(('Enter a valid command: ' + str(COMMANDS) + '\n').encode())
    print('Client ' + address + ' disconnected')
    client.close()
    sys.exit(0)


def init_server():
    port = set_port()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', port))
    address = socket.gethostbyname(socket.getfqdn())
    print('Server started at ' + address + ' on port ' + str(port))

    lock = Lock()
    while True:
        server.listen(10)
        client, connection = server.accept()
        print('Client ' + connection[0] + ' connected')
        process = Process(target=init_client, args=(lock, client, connection[0]))
        process.start()


init_server()
