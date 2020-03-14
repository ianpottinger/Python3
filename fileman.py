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
import os
import pathlib
import string
import doctest
import unittest
import pdb
import traceback
import shutil
import tempfile
import glob

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


def file_exists(filename: string) -> bool:
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
        return len(subject.readlines())
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
        append_file(filename, link)


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


class safe_open(object):
    def __init__(self, path, mode = 'w+b'):
        self._target = path
        self._mode = mode

    def __enter__(self):
        self._file = tempfile.NamedTemporaryFile(self._mode, delete = False)
        return self._file

    def __exit__(self, exc_type, exc_value, traceback):
        self._file.close()
        if exc_type is None:
            os.rename(self._file.name, self._target)
        else:
            self._target = self._target + '.recovered {datetime.datetime.today().time()}'
            os.rename(self._file.name, self._target)
            #os.unlink(self._file.name)


def append_file(filename, data):
    if file_exists(filename):
        with safe_open(filename, "a") as out:
            out.write(data)
    else:
        return -1


def create_file(filename):
    if not file_exists(filename):
        safe_open(filename, "w").close()
    else:
        return -1


def write_file(filename, data):
    if file_exists(filename):
        with safe_open(filename, 'w') as out:
            out.write(data)
    else:
        return -1


def write_binary_file(filename, data):
    if file_exists(filename):
        with safe_open(filename, 'wb') as out:
            out.write(data).close()
    else:
        return -1


def copy_file(source_file, destination_path):
    if file_exists(source_file):
        if directory_exists(destination_path):
            shutil.copyfile(source_file, destination_path)
        else:
            return 0
    else:
        return -1


def rename_file(source_file, destination_path):
    if file_exists(source_file):
        if directory_exists(destination_path):
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


def directory_exists(directory_path) -> bool:
    return os.path.isdir(directory_path)


def list_directory(directory_path: string):
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


def current_directory() -> object:
    return os.getcwd()


def set_directory(directory_path):
    return os.chdir(directory_path)


def create_directory(directory_path):
    if not directory_exists(directory_path):
        print(directory_path)
        os.mkdir(directory_path)
    else:
        return -1


def create_directories(directory_path):
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


def remove_directories(directory_path):
    if directory_exists(directory_path):
        os.removedirs(directory_path)
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
    # os.fdopen(tempfile, 'w+')


def close_temp(tempofile):
    os.close(tempofile)


def spool_temp(tempdata):
    with tempfile.SpooledTemporaryFile(max_size = 32) as temp:
        for i in range(len(tempdata)):
            temp.write(tempdata)

        temp.seek(0)
        return (temp.read())
    

def release_temp(tempname):
    os.unlink(tempname)


if __name__ == '__main__':
    doctest.testmod()
    unittest.main(exit=False)
    current_directory()
