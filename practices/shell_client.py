#!/usr/bin/python

import getopt
import socket
import sys
from datetime import datetime


def create_client():
    (opts, args) = getopt.getopt(sys.argv[1:], 'l:')
    log_path = None
    for (option, value) in opts:
        if option == '-l':
            log_path = value

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((socket.gethostname(), 8080))
    print("Enter command 'exit' to leave the program")
    command = ''
    while command != 'exit':
        command = str(input('> '))
        client.send(command.encode('ascii'))
        print(client.recv(4096).decode('ascii'))
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        with open(log_path, 'a') as file:
            file.write('[' + now + '] - ' + command + '\n')


create_client()
