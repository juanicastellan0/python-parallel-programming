#!/usr/bin/python

import sys
import getopt
import subprocess as sp
import time


class OptionsWithoutEntering(Exception):
    msg = "the options that must be entered:" \
          "\n-c : command" \
          "\n-o : output file" \
          "\n-l : log file"

    pass


class Proc:
    command = None
    output_file = None
    log_file = None
    stderr = None

    def run(self):
        (opts, args) = getopt.getopt(sys.argv[1:], 'c:o:l:')

        if len(opts) < 3:
            raise OptionsWithoutEntering()

        for (option, value) in opts:
            if option == '-c':
                self.command = value
            elif option == '-o':
                self.output_file = open(value, 'a')
            elif option == '-l':
                self.log_file = open(value, 'a')

        process = sp.Popen([self.command], stdout=self.output_file, stderr=sp.PIPE, shell=True)
        self.stderr = process.communicate()[1]
        if not self.stderr:
            self.log_file.write(str(time.asctime()) + ': Comando "' + self.command + '" ejecutado correctamente')
        else:
            self.log_file.write(str(time.asctime()) + ': ' + self.stderr)


proc = Proc()

try:
    proc.run()
except getopt.GetoptError as error:
    print(error.msg)
    print(OptionsWithoutEntering.msg)
except OptionsWithoutEntering as error:
    print(error.msg)

print('command "' + proc.command + '" executed '
      + ('successfully, check ' + proc.output_file.name + ' for see output' if not proc.stderr
         else 'with errors, check ' + proc.log_file.name + ' for more info'))
