#!/usr/bin/python

from sys import exit
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, getfqdn
from threading import Lock, Thread, current_thread
from datetime import datetime
from subprocess import Popen, PIPE


def connect():
    alice_sock = socket(AF_INET, SOCK_STREAM)
    alice_sock.bind(('', 8080))
    ip = gethostbyname(getfqdn())
    print('Alice connected at ' + ip + ' on port 8080 and is waiting for Bobs')

    return alice_sock


def manage_messages(bob_sock: socket, lock: Lock, bob_id):
    with open('etc_23/alice_threads_log.txt', 'a') as alice_threads_log:
        lock.acquire()
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        alice_threads_log.write(f'- {now}: {current_thread().name}\n')
        with Popen(
                ['ps -eLf | grep alice_threads.py | grep -v grep'],
                shell=True,
                universal_newlines=True,
                stdout=PIPE
        ) as subprocess:
            stdout, stderr = subprocess.communicate()
            alice_threads_log.write(stdout)
            stderr_string = stderr if stderr else 'without errors'
            alice_threads_log.write(stderr_string + '\n')
        lock.release()

    while True:
        get_message(bob_sock, bob_id)
        send_message(bob_sock, bob_id)


def get_message(bob_sock: socket, bob_id):
    while True:
        message = bob_sock.recv(1024).decode()
        if message == 'cambio':
            break
        elif message == 'exit':
            print('Connection finished for ' + str(bob_id))
            exit(0)
        print('\t- Bob ' + str(bob_id) + ': ' + message)


def send_message(bob_sock: socket, bob_id):
    while True:
        message = input('- (For Bob ' + str(bob_id) + ') Alice: ').encode()
        bob_sock.send(message)
        if message.decode() == 'cambio':
            break
        elif message.decode() == 'exit':
            exit(0)


def start_walkie_talkie():
    alice_sock = connect()
    alice_sock.listen(16)
    lock = Lock()
    bob_id = 0
    while True:
        bob_sock, bob_ip = alice_sock.accept()
        bob_id += 1
        print('Bob connected at ' + bob_ip[0] + ':' + str(bob_ip[1]))
        thread = Thread(target=manage_messages, args=(bob_sock, lock, bob_id))
        thread.start()


start_walkie_talkie()
