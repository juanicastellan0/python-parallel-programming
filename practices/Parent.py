#!/usr/bin/python

import os
import sys
import time
import getopt


class Parent:
    children_qty = 1

    def __init__(self):
        print('I am the parent with pid: ' + str(os.getpid()) + ' (on init)')
        (opts, args) = getopt.getopt(sys.argv[1:], 'n:')
        if len(opts) == 1:
            for (option, value) in opts:
                if option == '-n':
                    self.children_qty = int(value)

    def gen_child(self):
        if self.children_qty < 1:
            fork = os.fork()
            if fork == 0:
                self.child_fun()
        else:
            for i in range(self.children_qty):
                fork = os.fork()
                if fork == 0:
                    self.other_child_fun()

    @staticmethod
    def child_fun():
        for i in range(5):
            print('I am the child with pid: ' + str(os.getpid()))
            time.sleep(1)
        os._exit(0)

    @staticmethod
    def other_child_fun():
        print('I am the child with pid: ' + str(os.getpid())
              + ' and my parent pid is: ' + str(os.getppid()))
        time.sleep(1)
        os._exit(0)

    @staticmethod
    def wait():
        time.sleep(2)
        print('I am the parent with pid: ' + str(os.getpid()) + ' (on wait)')
        # print('Waiting for completion of my child process...')
        time.sleep(1)
        child_pid, status = os.wait()
        print('Child process with pid: ' + str(child_pid) + ' completed with status: ' + str(status))


try:
    parent = Parent()
    parent.gen_child()
    if parent.children_qty == 1:
        parent.wait()
except getopt.GetoptError as error:
    print('\n Error: ' + error.msg)
