#!/usr/bin/python

import os
import string
import sys
import time
from getopt import getopt
from multiprocessing import Lock, Process


def set_options():
    processes_qty = file_name = iterations_qty = None
    opts, args = getopt(sys.argv[1:], 'n:f:r:')

    if len(opts) < 3:
        print("the options that must be entered:" + "\n-n : process quantity" + "\n-f : file name"
              + "\n-r : iterations quantity")
        sys.exit(0)

    for (option, value) in opts:
        if option == '-n':
            processes_qty = int(value)
        elif option == '-f':
            file_name = value
        elif option == '-r':
            iterations_qty = int(value)

    return processes_qty, file_name, iterations_qty


def write_letters(lock, file_name, iterations_qty, letter):
    lock.acquire()
    with open(file_name, 'a') as file:
        for n in range(iterations_qty):
            time.sleep(0.1)
            file.write(letter)
            file.flush()
    lock.release()


def write_alphabet():
    processes_qty, file_name, iterations_qty = set_options()
    alphabet = string.ascii_uppercase
    lock = Lock()
    processes = []

    os.system('rm ' + file_name) if os.path.isfile(file_name) else os.system('touch ' + file_name)

    for n in range(processes_qty):
        process = Process(target=write_letters, args=(lock, file_name, iterations_qty, alphabet[n]))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


write_alphabet()
