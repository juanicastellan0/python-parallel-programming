#!/usr/bin/python

import sys
import getopt


class OptionsWithoutEntering(Exception):
    msg = "the options that must be entered:" \
          "\n-a : number a" \
          "\n-b : number b" \
          "\n-o : operation"

    pass


class WrongOperation(Exception):
    @staticmethod
    def get_message(wrong, valid):
        return "you entered: " + wrong + ", valid operations: " + valid

    pass


class Calc:
    VALID_OPS = ['+', '-', 'x', '/']
    a = b = result = 0
    op = ''

    def set_opts(self):
        (opts) = getopt.getopt(sys.argv[1:], 'a:b:o:')

        if len(opts) < 3:
            raise OptionsWithoutEntering()

        for (option, value) in opts:
            if option == '-a':
                self.a = int(value)
            elif option == '-b':
                self.b = int(value)
            elif option == '-o':
                if value not in self.VALID_OPS:
                    raise WrongOperation()
                self.op = value

    def calculate(self):
        a = self.a
        b = self.b
        op = self.op

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == 'x':
            result = a * b
        else:
            result = a / b

        self.result = result

        print(self.a, self.op, self.b, "=", self.result)


calc = Calc()
try:
    calc.set_opts()
    calc.calculate()
except OptionsWithoutEntering as exception:
    print(exception.msg)
except getopt.GetoptError as exception:
    print(exception.msg)
    print(OptionsWithoutEntering.msg)
