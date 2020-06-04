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
