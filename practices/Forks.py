#!/usr/bin/python

import os, time


class Fork:
    def __init__(self, child_qty=0):
        self.child_qty = child_qty
        print('I am the parent with pid: ', os.getpid())
        self.newp = os.fork()

    def gen_process(self):
        print('generando ', self.child_qty, ('procesos hijos' if self.child_qty > 1 else 'proceso hijo'))
        while True:
            newp = os.fork()
            if newp == 0:
                self.check_child()
            else:
                print('parent: ', os.getpid(), 'child: ', newp)

            reply = input('q for quit / c for new fork')

            if reply == 'c':
                continue
            else:
                break