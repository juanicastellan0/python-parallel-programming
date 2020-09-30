#!/usr/bin/python

from string import ascii_uppercase
from multiprocessing import Lock
from os import system, path
from threading import Thread, main_thread
from threading import enumerate as threads_enumerate
from getopt import getopt
from sys import argv, exit
from time import sleep
from datetime import datetime as dt
from subprocess import Popen, PIPE


def set_options():
    threads_qty = file_name = iterations_qty = None
    opts, args = getopt(argv[1:], 'n:f:r:')

    if len(opts) < 3:
        print("the options that must be entered:" + "\n-n : threads quantity" + "\n-f : file name"
              + "\n-r : iterations quantity")
        exit(0)

    for (option, value) in opts:
        if option == '-n':
            threads_qty = int(value)
        elif option == '-f':
            file_name = value
        elif option == '-r':
            iterations_qty = int(value)

    return threads_qty, file_name, iterations_qty


def log_threading(threads_qty):
    now = dt.now().strftime("%d/%m/%Y %H:%M:%S")
    with open('etc_23/log_threading.txt', 'w+') as log_threading_file:
        log_threading_file.write(f'alphabet_threads: {now}\n')
        log_threading_file.write(f'threads quantity: {threads_qty}\n')
        with Popen(
                ['ps -eLf | grep alphabet_threads | grep -v grep'],
                shell=True,
                universal_newlines=True,
                stdout=PIPE
        ) as subprocess:
            stdout, stderr = subprocess.communicate()
            log_threading_file.write(stdout)
            stderr_string = stderr if stderr else 'without errors'
            log_threading_file.write(stderr_string)


def write_letters(lock, file_name, iterations_qty, letter):
    lock.acquire()
    with open(file_name, 'a') as file:
        for n in range(iterations_qty):
            sleep(0.1)
            file.write(letter)
            file.flush()
    lock.release()


def write_alphabet():
    threads_qty, file_name, iterations_qty = set_options()
    lock = Lock()
    system('rm ' + file_name) if path.isfile(file_name) else system('touch ' + file_name)
    for n in range(threads_qty):
        thread = Thread(target=write_letters, args=(lock, file_name, iterations_qty, ascii_uppercase[n]))
        thread.start()
    log_threading(len(threads_enumerate()))
    for thread in threads_enumerate():
        if thread == main_thread():
            continue
        thread.join()


write_alphabet()
