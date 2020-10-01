#!/usr/bin/python

from getopt import getopt, GetoptError
from sys import argv, exit
from multiprocessing import Process, current_process


def get_options():
    processes_qty = min_num = max_num = None
    opts, args = getopt(argv[1:], 'p:m:n:')
    if len(opts) != 3:
        print("the options that must be entered:" + "\n-p : processes quantity" + "\n-m : minimum number"
              + "\n-n : maximum number")
        exit(0)
    for (opt, arg) in opts:
        if int(arg) < 0:
            raise ValueError
        if opt == '-p':
            processes_qty = int(arg)
        elif opt == '-m':
            min_num = int(arg)
        elif opt == '-n':
            max_num = int(arg)
    if min_num > max_num:
        raise GetoptError('Minimum number can`t be higher than maximum number')
    if processes_qty > max_num - min_num:
        raise GetoptError('Processes quantity can`t be higher than the numbers to process')

    return processes_qty, min_num, max_num


def square_numbers(numbers):
    for number in numbers:
        print(current_process().name + ': \t' + str(number) + '²' + ' = ' + str(number ** 2))


def calculate_square():
    processes_qty, min_num, max_num = get_options()
    processes = []
    numbers = list(range(min_num, max_num))
    size = len(numbers)
    numbers_lists = [numbers[i * size // processes_qty:(i + 1) * size // processes_qty] for i in range(processes_qty)]
    for sublist in numbers_lists:
        process = Process(target=square_numbers, args=(sublist,))
        process.start()
        processes.append(process)
    for p in processes:
        p.join()


calculate_square()
