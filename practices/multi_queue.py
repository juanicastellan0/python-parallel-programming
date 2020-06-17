# !/usr/bin/python

import multiprocessing
import time
import os


def get_process_info(n, queue):
    print('Proceso ' + str(n) + ', PID: ' + str(os.getpid()))
    time.sleep(n)
    queue.put(str(os.getpid()) + '\t')


def create_queue():
    queue = multiprocessing.Queue()
    procs = []
    for n in range(10):
        proc = multiprocessing.Process(target=get_process_info, args=(n, queue))
        procs.append(proc)
        proc.start()
        proc.join()
    while not queue.empty():
        print(queue.get(), end='')


create_queue()
