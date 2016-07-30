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

import builtins, keyword, os, sys, time
import queue, heapq, collections, threading, pickle, concurrent
import numbers, operator, math, cmath, decimal, fractions, random, itertools
import string, textwrap, re, unicodedata, locale, uuid, hashlib, binascii, zlib
import doctest, unittest, cProfile, timeit, logging, traceback, datetime
import socket, ftplib, poplib, nntplib, smtplib, telnetlib, email, functools
import argparse, calendar, pprint, struct, copy, pdb, socket, subprocess
import ipaddress, tkinter#, dateutil, numpy, scipy, pygame, matplotlib, pygobject

DEBUG_MODE = False
if DEBUG_MODE == True:
    pdb.set_trace()

RESERVED = ["and", "del", "from", "not", "while", "as", "elif",
            "global", "or", "with", "assert", "else", "if", "pass",
            "yield", "break","except", "import", "print", "class",
            "exec", "in", "raise", "continue", "finally", "is",
            "return", "def", "for", "lambda", "try"]

import shutil, tempfile, glob



def file_exists(filename):
    return os.path.isfile(filename)

def read_binary_file(filename):
    if file_exists(filename):
        return open(filename, "rb").read()
    else:
        return -1

def read_text_file(filename):
    if file_exists(filename):
        return open(filename, "r").readlines()
    else:
        return -1

def file_lines(filename):
    if file_exists(filename):
        subject = open(filename)
        return len(subject.readlines() )
    else:
        return -1

def file_to_set(filename):
    content = set()
    if file_exists(filename):
        with open(filename, 'rt') as lines:
            for line in lines:
                content.add(line.replace('\n', ''))
        return content
    else:
        return -1

def set_to_line(filename, lines):
    empty_file(filename)
    for link in sorted(lines):
        append_file(filename, line)

def file_size(filename):
    if file_exists(filename):
        return os.path.getsize(filename)
    else:
        return -1

def file_extension(filepath):
    if file_exists(filepath):
        
        return os.path.splitext(filepath)[-1]
    else:
        return -1

def append_file(filename, data):
    if file_exists(filename):
        with open(filename,"a") as out:
            out.write(data)
    else:
        return -1

def create_file(filename):
    if not file_exists(filename):
        open(filename, "w").close()
    else:
        return -1

def write_file(filename, data):
    if file_exists(filename):
        with open(filename, 'w') as out:
            out.write(data)
    else:
        return -1

def write_binary_file(filename, data):
    if file_exists(filename):
        with open(filename, 'wb') as out:
            out.write(data).close()
    else:
        return -1

def copy_file(source_file, destination_path):
    if file_exists(source_file):
        if directory_exists(directory_path):
            shutil.copyfile(source_file, destination_path)
        else:
            return 0
    else:
        return -1

def rename_file(source_file, destination_path):
    if file_exists(source_file):
        if directory_exists(directory_path):
            os.rename(source_file, destination_path)
        else:
            return 0
    else:
        return -1

def delete_file(filename):
    """pathfilename string"""
    if file_exists(filename):
        os.unlink(filename)
    else:
        return -1

def empty_file(filename):
    if not file_exists(filename):
        return -1
    else:
        open(filename, "w").close()

        

def directory_exists(directory_path):
    return os.path.isdir(directory_path)

def list_directory(directory_path):
    if directory_exists(directory_path):
        return os.listdir(directory_path)  
    else:
        return -1
  
def scan_directory(directory_path):
    if directory_exists(directory_path):
        return [item.name for item in os.scandir(directory_path)]
    else:
        return -1
  
def list_search(directory_search):
    return glob.glob(directory_search)

def current_directory():
    return os.getcwd()

def create_directory(directory_path):
    if not directory_exists(directory_path):
        print(directory_path)
        os.mkdir(directory_path)
    else:
        return -1

def remove_directory(directory_path):
    if directory_exists(directory_path):
        os.rmdir(directory_path)
    else:
        return -1

def remove_tree(directory_path):
    if directory_exists(directory_path):
        shutil.rmtree(directory_path)
    else:
        return -1



def object_exists(filepath):  
    return os.path.exists(filepath)

def copy_object(source, destination):
    shutil.copyfileobj(source, destination)  



def create_temp(extension):
    tempofile, tempname = tempfile.mkstemp(extension)
    return tempofile, tempname

def write_temp(tempofile, data):
    os.write(tempofile, data)
    #os.fdopen(tempfile, 'w+')

def close_temp(tempofile):
    os.close(tempofile)

def release_temp(tempname):
    os.unlink(tempname)  



if __name__ == '__main__':
    doctest.testmod()
    unittest.main(exit=False)













