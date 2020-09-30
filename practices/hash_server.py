#!/usr/bin/python

from socket import socket, gethostbyname, getfqdn, AF_INET, SOCK_STREAM
from getopt import getopt
import sys
import hashlib

HASH_FUNCTIONS = {
    "sha1": hashlib.sha1(),
    "sha224": hashlib.sha224(),
    "sha256": hashlib.sha256(),
    "sha384": hashlib.sha384(),
    "sha512": hashlib.sha512(),
    "sha3-224": hashlib.sha3_224(),
    "sha3-256": hashlib.sha3_256(),
    "sha3-384": hashlib.sha3_384(),
    "sha3-512": hashlib.sha3_512()
}


def get_options():
    port = None
    with_threading = False
    opts, args = getopt(sys.argv[1:], 'p:m')
    print("the options that must be entered:" + "\n-p : port" + "\n-m : with multiprocessing")
    for (opt, arg) in opts:
        if opt == '-p':
            port = int(arg)
        elif opt == '-m':
            with_threading = False

    return port, with_threading


def hash_text(client_sock):
    hash_func = client_sock.recv(64).decode()
    if hash_func not in HASH_FUNCTIONS:
        client_sock.send('404'.encode())
        return
    client_sock.send('200'.encode())
    hasher = HASH_FUNCTIONS[hash_func]
    hasher.update(client_sock.recv(1024))
    client_sock.send(hasher.hexdigest().encode())


def launch_server():
    ip = gethostbyname(getfqdn())
    port, with_threading = get_options()
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    print('Server on: ' + ip + ':' + str(port) + ' with ' + ('threads' if with_threading else 'processes'))
    if with_threading:
        from threading import Thread as Process
    else:
        from multiprocessing import Process
    while True:
        sock.listen(16)
        client_sock, ip = sock.accept()
        print('Connected from ' + ip[0])
        process = Process(target=hash_text, args=(client_sock,))
        process.start()


launch_server()
