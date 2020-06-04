#!/usr/bin/python

import sys
import getopt


class OptionsWithoutEntering(Exception):
    msg = "the options that must be entered:" \
          "\n-i : input file" \
          "\n-o : output file"

    pass


class Copy:
    i_file = None
    o_file = None

    def cp(self):
        (opts, args) = getopt.getopt(sys.argv[1:], 'i:o:')

        if len(opts) < 2:
            raise OptionsWithoutEntering()

        for (option, file_name) in opts:
            if option == '-i':
                self.i_file = open(file_name)
            elif option == '-o':
                self.o_file = open(file_name, 'w')

        for line in self.i_file:
            self.o_file.write(line)


copy = Copy()

try:
    copy.cp()
except IOError as error:
    print(error)
