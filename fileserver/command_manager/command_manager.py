import socket
from subprocess import Popen, PIPE


def manage_commands(client: socket):
    while True:
        command = client.recv(4096).decode('ascii')
        print('Command received: ' + command)
        if command == 'exit':
            client.send('Server closed'.encode('ascii'))
            break
        with Popen([command], shell=True, universal_newlines=True, stdout=PIPE, stderr=PIPE) as process:
            stdout, stderr = process.communicate()
            client.send(('OK\n' + stdout).encode('ascii')) if process.returncode == 0 \
                else client.send(('ERROR\n' + stderr).encode('ascii'))
    print('Client ' + str(client) + ' disconnected!')
    client.close()
