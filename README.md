# python-parallel-programming
Practice of parallel programming with python in "Computación II" from Universidad de Mendoza

```bash
git clone https://github.com/juanicastellan0/python-parallel-programming.git
```

## tag: GETOPT

```bash
git checkout tags/GETOPT
```

## tag: ej3 (subprocess Popen)

```bash
git checkout tags/ej3
```

## tag: fork

```bash
git checkout tags/fork
cd practices
# ej 4:
python Parent.py
# ej 5:
python Parent.py -n 3
```

## tag: signal

```bash
git checkout tags/signal
cd practices
# ej 6:
python Parent.py --send
# ej 7:
python Parent.py -n 2
# ej 8:
python Parent.py -n 3 --send
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
