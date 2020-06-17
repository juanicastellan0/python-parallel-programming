#!/usr/bin/python

import os
import sys
import time
import signal
from multiprocessing import Process, Pipe
from multiprocessing.connection import Connection


def send_msg(writer: Connection, fileno):
    sys.stdin = os.fdopen(fileno)
    while True:
        time.sleep(0.5)
        msg = input('>>> ')
        if msg != 'exit':
            print('Sending from PID: ' + str(os.getpid()))
            writer.send(msg)
        else:
            break


def receive_msg(reader: Connection):
    while True:
        msg = reader.recv()
        print('Reading from PID: ' + str(os.getpid()))
        print('Message: ' + msg)


def create_processes():
    print('Write messages to send through the Pipe (type "exit" to quit)')
    reader, writer = Pipe()
    fn = sys.stdin.fileno()
    w_proc = Process(target=send_msg, args=(writer, fn))
    r_proc = Process(target=receive_msg, args=(reader,))
    w_proc.start()
    r_proc.start()
    w_proc.join()
    os.kill(r_proc.pid, signal.SIGTERM)


create_processes()
