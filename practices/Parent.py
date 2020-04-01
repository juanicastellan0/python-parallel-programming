#!/usr/bin/python

import os
import time


class Parent:
    fork = None

    def __init__(self):
        print('I am the parent with pid: ' + str(os.getpid()) + ' (on init)')

    def gen_child(self):
        self.fork = os.fork()
        if self.fork == 0:
            print('(is the child)')
            self.child_fun()
        else:
            print('(is the parent)')

    @staticmethod
    def child_fun():
        for i in range(5):
            print('I am the child with pid: ' + str(os.getpid()))
            time.sleep(1)
        os._exit(0)

    @staticmethod
    def wait():
        print('I am the parent with pid: ' + str(os.getpid()) + ' (on wait)')
        print('Waiting for completion of my child process...')
        child_pid, status = os.wait()
        print('Child process with pid: ' + str(child_pid) + ' completed with status: ' + str(status))


parent = Parent()
parent.gen_child()
parent.wait()

'''
se ejecuta un proceso y se le hace fork para crear un hijo
el fork crea un proceso hijo y devuelve el id al padre, le indicamos que espere a que termine el hijo
el fork también le devuelve 0 al hijo, entonces podemos hacer que el hijo haga su propia función
'''