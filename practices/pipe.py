#!/usr/bin/python

import os
import signal
import sys
import time


class Pipe:
    r, w = None, None
    sigusr1_received = False
    sigusr2_received = False

    def __init__(self):
        self.read_fd, self.write_fd = os.pipe()

    def child_handler(self, signum, stack):
        self.sigusr1_received = True

    def parent_handler(self, signum, stack):
        self.sigusr2_received = True

    def send_messages_between_process(self):
        # PROCESS A
        pid_a = os.getpid()
        print('process A ' + str(pid_a) + ' created!')
        signal.signal(signal.SIGUSR1, self.child_handler)
        signal.signal(signal.SIGUSR2, self.parent_handler)
        # FIRST FORK
        pid_b = os.fork()
        if pid_b > 0:  # PROCESS A SEND SIGUSR1 TO PROCESS B
            print('process B ' + str(pid_b) + ' created!')
            time.sleep(2)
            print('process A sending a sigusr1 to process B ' + str(pid_b))
            os.kill(pid_b, signal.SIGUSR1)
            print('process A is waiting for a sigusr2...')
            while True:  # PROCESS A WAIT FOR SIGUSR2
                signal.pause()
                if self.sigusr2_received:  # PROCESS A READ AND SHOW PIPE MESSAGES
                    print('process A with PID=' + str(os.getpid()) + ' is reading the pipe...')
                    time.sleep(1)
                    os.close(self.write_fd)
                    read_fd = os.fdopen(self.read_fd)
                    msg = read_fd.read()
                    if not msg:
                        print("Empty message.")
                    else:
                        print("Message: " + msg)
                    sys.exit(0)
        else:  # PROCESS B
            # SECOND FORK
            pid_c = os.fork()
            if pid_c > 0:  # PROCESS B WAIT FOR SIGUSR1
                print('process C ' + str(pid_c) + ' created!')
                print('process B is waiting for a sigusr1...')
                while True:
                    signal.pause()
                    if self.sigusr1_received:  # PROCESS B WRITE MESSSAGE 1 IN PIPE
                        self.sigusr1_received = False
                        print('process B is writing on the pipe...')
                        os.close(self.read_fd)
                        write_fd = os.fdopen(self.write_fd, 'w')
                        msg = '\nMessage 1 PID=' + str(os.getpid())
                        write_fd.write(msg)
                        write_fd.close()
                        # PROCESS B SEND SIGUSR1 TO PROCESS C
                        print('process B will send a sigusr1 to process C ' + str(pid_c))
                        time.sleep(1)
                        os.kill(pid_c, signal.SIGUSR1)
            else:  # PROCESS C
                while True:  # PROCESS C WAIT FOR SIGUSR1
                    print('process C is waiting for a sigusr1...')
                    signal.pause()
                    if self.sigusr1_received:  # PROCESS C WRITE MESSAGE 2 IN PIPE
                        self.sigusr1_received = False
                        print('process C is writing on the pipe...')
                        os.close(self.read_fd)
                        msg = '\nMessage 2 PID=' + str(os.getpid())
                        write_fd = os.fdopen(self.write_fd, 'w')
                        write_fd.write(msg)
                        write_fd.close()
                        # PROCESS C SEND SIGUSR2 TO PROCESS A
                        print('process C will send a sigusr2 to process A ' + str(pid_a))
                        time.sleep(1)
                        os.kill(pid_a, signal.SIGUSR2)

    def enter_a_message(self):
        os.close(self.read_fd)
        msg = input("Enter a message:")
        os.write(self.write_fd, msg.encode())

    def show_message(self):
        os.close(self.write_fd)
        msg = os.fdopen(self.read_fd).readline()
        if not msg:
            print("Empty message.")
        else:
            print("\nMessage: " + msg)

    def send_message_to_child(self):
        pid = os.fork()
        if pid > 0:
            time.sleep(1)
            self.enter_a_message()
            print("Parent sending a message to child... ")
            time.sleep(1)
        else:
            print("\nChild process is reading... \n")
            time.sleep(1)
            self.show_message()


pipe = Pipe()
# pipe.enter_a_message()
# pipe.show_message()
# pipe.send_message_to_child()
pipe.send_messages_between_process()
