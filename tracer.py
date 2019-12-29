#! /usr/bin/env python		#Allow Unix shell to execute as a Python script
# _*_ coding: UTF-8 _*_		#Enable unicode encoding

__author__ = "Ian Pottinger"
__date__ = "20/12/2012"
__contact__ = "ianpottinger@me.com"
__version__ = "1.3.5.7.9 even avoidance"
__credits__ = "Commonly known as Potts"
__copyright__ = "Copyleft for balance"
__license__ = "Whatever Potts Decides"
__metadata__ = [__author__, __date__, __contact__, __version__,
                __credits__, __copyright__, __license__]


import keyword
import trace
import collections

DEBUG_MODE = True
if DEBUG_MODE:
    import pdb
    #pdb.set_trace()
    import logging
    FORMAT = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
    logging.basicConfig(level = logging.INFO, format = FORMAT)
    #logging.basicConfig(level = logging.WARNING, format = FORMAT)
    #logging.basicConfig(level = logging.DEBUG, format = FORMAT)
    #logging.basicConfig(level = logging.ERROR, format = FORMAT)
    #logging.basicConfig(level = logging.CRITICAL, format = FORMAT)

RESERVED = ['False', 'None', 'True', 'and', 'as', 'assert', 'break',
            'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec',
            'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
            'lambda', 'nonlocal', 'not', 'or', 'pass', 'print',
            'raise', 'return', 'try', 'while', 'with', 'yield']
KEYWORDS = keyword.kwlist


def report_tracing(func, *args, **kwargs):
    outputs = collections.defaultdict(list)

    tracing = trace.Trace(trace = True)
    tracing.runfunc(func, *args, **kwargs)

    traced = collections.defaultdict(set)
    for filename, line in tracing.results().counts:
        traced[filename].add(line)

    for filename, tracedline in traced.items():
        with open(filename) as file:
            for idx, fileline in enumerate(file, start = 1):
                outputs[filename].append((idx, idx in tracedlines, fileline))

    return outputs


def print_traced_execution(tracings):
    for filename, tracing in tracings.items():
        print(filename)
        for idx, executed, content in tracing:
            print('{}{}   {}'.format(idx,
                                     '+' if executed else ' ',
                                     content),
                  end =  '')
            print()


