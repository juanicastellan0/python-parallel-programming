# !/usr/bin/python

import sys
from getopt import getopt
from multiprocessing import Process, Lock, Value, Semaphore
import time
import random


def patient_entering(surgeries, enter: Value, enter_lock):
    surgeries.acquire()
    print('Paciente entrando... Consultorios disponibles: ' + str(surgeries.get_value()))
    enter_lock.acquire()
    enter.value = enter.value + 1
    enter_lock.release()
    print('Entro el paciente: ' + str(enter.value))


def patient_leaving(surgeries, out: Value, out_lock):
    surgeries.release()
    print('Paciente saliendo... Consultorios disponibles: ' + str(surgeries.get_value()))
    out_lock.acquire()
    out.value = out.value + 1
    out_lock.release()
    print('Salio el paciente: ' + str(out.value))


def going_in(surgeries, enter: Value, enter_lock, min_arrival_value, max_arrival_value):
    while True:
        time.sleep(random.randint(min_arrival_value, max_arrival_value))
        incoming_patient = Process(target=patient_entering, args=(surgeries, enter, enter_lock))
        incoming_patient.start()


def going_out(surgeries, out: Value, out_lock, min_departure_value, max_departure_value):
    while True:
        print('Paciente siendo atendido...')
        time.sleep(random.randint(min_departure_value, max_departure_value))
        outgoing_patient = Process(target=patient_leaving, args=(surgeries, out, out_lock))
        outgoing_patient.start()


def init_wait():
    surgeries_qty = 5
    min_arrival = 1
    max_arrival = 3
    min_departure = 5
    max_departure = 7

    opts, args = getopt(sys.argv[1:], 'a:b:c:d:e:')

    for (opt, value) in opts:
        if opt == '-a':
            surgeries_qty = int(value)
        elif opt == '-b':
            min_arrival = int(value)
        elif opt == '-c':
            max_arrival = int(value)
        elif opt == '-d':
            min_departure = int(value)
        elif opt == '-e':
            max_departure = int(value)

    enter = Value('d', 0)
    out = Value('d', 0)
    surgeries_available = Semaphore(surgeries_qty)
    enter_lock = Lock()
    out_lock = Lock()

    print('Consultorios disponibles: ' + str(surgeries_available.get_value()))
    enter_process = Process(target=going_in, args=(surgeries_available, enter, enter_lock, min_arrival, max_arrival))
    out_process = Process(target=going_out, args=(surgeries_available, out, out_lock, min_departure, max_departure))
    enter_process.start()
    out_process.start()


init_wait()
