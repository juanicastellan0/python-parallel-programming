#!/usr/bin/python

import os
import sys
import time
import getopt
import signal


class Parent:
    children_qty = 1
    ping_received = False
    send_activated = False
    sigusr_received = False
    child_pid = 0
    child_pids = []

    def __init__(self):
        print('I am the parent with pid: ' + str(os.getpid()) + ' (on init)')
        (opts, args) = getopt.getopt(sys.argv[1:], 'n:', ["send"])
        if len(opts) > 0:
            for (option, value) in opts:
                if option == '-n':
                    self.children_qty = int(value)
                elif option == '--send':
                    self.send_activated = True

    def control_children(self):
        if self.children_qty > 1:
            if self.send_activated:
                self.send_signal_to_children()
            else:
                if self.children_qty == 2:
                    self.ping_pong()
                else:
                    self.print_each_child_once()
        else:
            if self.send_activated:
                self.send_signal_to_child_each_five_seconds()
            else:
                self.print_a_child_five_times()

    def ping_pong(self):
        signal.signal(signal.SIGINT, self.parent_term_handler)
        fork1 = os.fork()
        if fork1 == 0:
            self.ping()
        else:
            self.child_pids.append(fork1)
            fork2 = os.fork()
            if fork2 == 0:
                signal.signal(signal.SIGUSR1, self.pong)
                while True:
                    signal.pause()
            else:
                self.child_pids.append(fork2)
                signal.signal(signal.SIGUSR1, self.receive_ping)
                while True:
                    signal.pause()
                    if self.ping_received:
                        os.kill(fork2, signal.SIGUSR1)

    @staticmethod
    def ping():
        for i in range(10):
            print('\nPING \t- Im the child 1 with PID: ' + str(os.getpid()))
            os.kill(os.getppid(), signal.SIGUSR1)
            time.sleep(1)
        os.kill(os.getppid(), signal.SIGINT)

    # child handler
    def pong(self, signum, stack):
        self.ping_received = False
        print('PONG \t- Im the child 2 with PID: ' + str(os.getpid()))

    # parent handler
    def receive_ping(self, signum, stack):
        self.ping_received = True

    def parent_term_handler(self, signum, stack):
        time.sleep(1)
        for pid in self.child_pids:
            os.kill(pid, signal.SIGTERM)
        os.kill(os.getpid(), signal.SIGTERM)

    def send_signal_to_children(self):
        children_pids = []
        for i in range(self.children_qty):
            fork = os.fork()
            if fork == 0:
                signal.signal(signal.SIGUSR2, self.show_message)
                while True:
                    signal.pause()
                    if self.sigusr_received:
                        os._exit(0)
            else:
                time.sleep(1)
                print('Creating child process with PID: ' + str(fork))
                children_pids.append(fork)

        for pid in children_pids:
            time.sleep(1)
            os.kill(pid, signal.SIGUSR2)

    def show_message(self, signum, stack):
        self.sigusr_received = True
        print('PID: ' + str(os.getpid()) + ' received signal: ' + str(signum) + ' from PPID: ' + str(os.getppid()))

    def parent_handler(self, signum, stack):
        print('Parent saying goodbye... ')
        time.sleep(1)
        os.kill(self.child_pid, signal.SIGTERM)
        os.kill(os.getpid(), signal.SIGTERM)

    @staticmethod
    def child_message(signum, stack):
        print('PID: ' + str(os.getpid()) + ' received signal: ' + str(signum) + ' from PPID: ' + str(os.getppid()))

    def send_signal_to_child_each_five_seconds(self):
        signal.signal(signal.SIGUSR1, self.child_message)
        fork = os.fork()
        if fork == 0:
            while True:
                signal.pause()
        else:
            self.child_pid = fork
            signal.signal(signal.SIGINT, self.parent_handler)
            for i in range(20):
                os.kill(fork, signal.SIGUSR1)
                time.sleep(1)
            os.kill(fork, signal.SIGTERM)

    @staticmethod
    def print_a_child_five_times():
        fork = os.fork()
        if fork == 0:
            for i in range(5):
                print('I am the child with pid: ' + str(os.getpid()))
                time.sleep(1)
            os._exit(0)
        else:
            time.sleep(2)
            print('I am the parent with pid: ' + str(os.getpid()) + ' (on wait)')
            # print('Waiting for completion of my child process...')
            time.sleep(1)
            child_pid, status = os.wait()
            print('Child process with pid: ' + str(child_pid) + ' completed with status: ' + str(status))

    def print_each_child_once(self):
        for i in range(self.children_qty):
            fork = os.fork()
            if fork == 0:
                print('I am the child with pid: ' + str(os.getpid())
                      + ' and my parent pid is: ' + str(os.getppid()))
                time.sleep(1)
                os._exit(0)


'''
try:
    parent = Parent()
    parent.control_children()
except getopt.GetoptError as error:
    print('\n Error: ' + error.msg)
'''
