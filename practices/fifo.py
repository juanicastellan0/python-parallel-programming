#!/usr/bin/python
import getopt
import os
import sys
import time


class Fifo:
    fifo_pipe = '/tmp/fifo_pipe'

    def __init__(self):
        if not os.path.exists(self.fifo_pipe):
            os.mkfifo(self.fifo_pipe)
        self.read_fd, self.write_fd = os.pipe()

    def produce(self, message):
        # PRODUCER STORE MSG IN FIFO
        print('producer storing message in fifo... ')
        fifo_file = os.open(self.fifo_pipe, os.O_WRONLY)
        os.write(fifo_file, message)
        time.sleep(1)

    def consume(self):
        # CONSUMER READ MSG FROM FIFO
        print('consumer reading message from fifo... ')
        fifo_file = open(self.fifo_pipe, 'r')
        msg = fifo_file.read()
        pid_child = os.fork()
        if pid_child > 0:  # CONSUMER SEND MSG VIA PIPE TO CHIHLD
            print('consumer sending message via pipe to child... ')
            os.close(self.read_fd)
            write_fd = os.fdopen(self.write_fd, 'w')
            write_fd.write(msg)
            write_fd.close()
        else:  # CHILD SHOW MSG
            print('child showing the message... ')
            os.close(self.write_fd)
            read_fd = os.fdopen(self.read_fd)
            pipe_msg = read_fd.read()
            if not pipe_msg:
                print("Empty message.")
            else:
                print("Message: " + pipe_msg)
            sys.exit(0)


fifo = Fifo()
(opts, args) = getopt.getopt(sys.argv[1:], '', ['producer=', 'consumer'])
for (option, value) in opts:
    if option == '--producer':
        fifo.produce(value)
    elif option == '--consumer':
        fifo.consume()


