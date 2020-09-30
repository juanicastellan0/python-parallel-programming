#!/usr/bin/python

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


def going_in(surgeries, enter: Value, enter_lock):
    while True:
        time.sleep(random.randint(1, 3))
        incoming_patient = Process(target=patient_entering, args=(surgeries, enter, enter_lock))
        incoming_patient.start()


def going_out(surgeries, out: Value, out_lock):
    while True:
        print('Paciente siendo atendido...')
        time.sleep(random.randint(5, 7))
        outgoing_patient = Process(target=patient_leaving, args=(surgeries, out, out_lock))
        outgoing_patient.start()


def init_wait():
    enter = Value('d', 0)
    out = Value('d', 0)
    surgeries_available = Semaphore(5)
    enter_lock = Lock()
    out_lock = Lock()

    print('Consultorios disponibles: ' + str(surgeries_available.get_value()))
    enter_process = Process(target=going_in, args=(surgeries_available, enter, enter_lock))
    out_process = Process(target=going_out, args=(surgeries_available, out, out_lock))
    enter_process.start()
    out_process.start()


init_wait()
