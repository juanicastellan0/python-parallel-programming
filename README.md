# python-parallel-programming
Practice of parallel programming with python in "Computación II" from Universidad de Mendoza

```bash
git clone https://github.com/juanicastellan0/python-parallel-programming.git
```

## tag: GETOPT
```bash
git checkout tags/GETOPT
cd practices
# ej 1:
python calc.py -a 5 -b 6 -o +
# ej 2:
python copy.py -i file1.txt -o file2.txt
```

## tag: ej3 (subprocess Popen)
```bash
git checkout tags/ej3
cd practices
python proc.py -c "ls" -o /tmp/salida -l /tmp/log
```

## tag: fork
```bash
git checkout tags/fork
cd practices
# ej 4:
python parent.py
# ej 5:
python parent.py -n 3
```

## tag: signal
```bash
git checkout tags/signal
cd practices
# ej 6:
python parent.py --send
# ej 7:
python parent.py -n 2
# ej 8:
python parent.py -n 3 --send
```

## tag: pipe
```bash
git checkout tags/signal
cd practices
# ej 9:
python pipe.py
# ej 10:
    # terminal 1:
    python fifo.py --producer hola
    # terminal 2:
    python fifo.py --consumer
```

## tag: cliente_juncotic
```bash
git checkout tags/cliente_juncotic
cd practices
# terminal 1
python server_compu2.py
# terminal 2
python stream_client.py localhost 8080
```

## tag: tcp_udp
```bash
git checkout tags/tcp_udp
cd practices
# terminal 1
python stdin_server.py -p 8080 -t tcp -f file.txt
# terminal 2
python stdin_client.py -a localhost -p 8080 -t tcp
```

## tag: remote_shell
```bash
git checkout tags/remote_shell
cd practices
# terminal 1
python shell_server.py
# terminal 2
python shell_client.py -l shell.txt
```

## tag: remote_shell_multiproc
```bash
git checkout tags/remote_shell_multiproc
cd practices
# terminal 1
python multi_shell_server.py
# terminal 2
python multi_shell_client.py -l shell.txt
# terminal 3
python multi_shell_client.py -l shell2.txt
```

## tag: mp_pipe
```bash
git checkout tags/mp_pipe
cd practices
python multi_pipe.py
```

## tag: mp_mq
```bash
git checkout tags/mp_mq
cd practices
python multi_queue.py
```

## tag: echo_inv
```bash
git checkout tags/echo_inv
cd practices
# terminal 1
python echo_inv_server.py -p 8080
# terminal 2
python echo_inv_client.py -h 127.0.0.1 -p 8080
```

## tag: time
```bash
git checkout tags/time
cd practices
python client_time.py -h time.nist.gov -p 13 -t tcp
```

## tag: lock
```bash
git checkout tags/lock
cd practices
python alphabet_lock.py -n 26 -f /tmp/alphabet.txt -r 3
```

## tag: sock_lock
```bash
git checkout tags/sock_lock
cd practices
# terminal 1
python client_lock.py -p 8080
# terminal 2
telnet 127.0.1.1 8080
# test commands
```

## tag: hosp
```bash
git checkout tags/hosp
cd practices
python hosp_v1.py
# or
python hosp_v2.py -a 10 -b 2 -c 6 -d 3 -e 9
```

## tag: walkie
```bash
git checkout tags/walkie
cd practices
# terminal 1
python alice.py
# terminal 2
python bob.py -i 127.0.1.1
```

## tag: th
```bash
git checkout tags/th
cd practices
# ej 19
python alphabet_threads.py -n 26 -f /tmp/alphabet.txt -r 3
# ej 22
# terminal 1
python alice_threads.py
# terminal 2
python bob.py -i 127.0.1.1
```

## tag: hash
```bash
git checkout tags/hash
cd practices
# terminal 1
python hash_server.py -p 8080
# terminal 2
python hash_client.py -a 127.0.1.1 -p 8080 -h sha1 -c "hi world"
```

## tag: pcuadrado
```bash
git checkout tags/pcuadrado
cd practices
python square_calc.py -p 3 -m 6 -n 100
```
