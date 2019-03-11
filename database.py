#!/usr/bin/env python3		#Allow Unix shell to execute as a Python script
# _*_ coding: UTF-8 _*_	#Enable unicode encoding

__author__ = "Ian Pottinger"
__date__ = "20/12/2012"
__contact__ = "ianpottinger@me.com"
__version__ = "1.3.5.7.9 even avoidance"
__credits__ = "Commonly known as Potts"
__copyright__ = "Copyleft for balance"
__license__ = "Whatever Potts Decides"
__metadata__ = [__author__, __date__, __contact__, __version__,
                __credits__, __copyright__, __license__]

import sqlite3
import psycopg2
import keyword

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


import fileman
import jason

ACID = ['Atomicity', 'Consistency', 'Isolation', 'Durability']


def create_database(engine, filepath, filename):
    if engine == "sqlite":
        pass
    elif engine == "postgre":
        pass
    else:
        pass
    
    database = filepath + filename
    return


def coonect_database(filepath, filename):
    database = filepath + filename
    return


def drop_database(database):
    return


def close_database(database):
    return


def create_table(databse, table_name):
    return


def drop_table(databse, table_name):
    return


def return_table(database, table_name):
    statement = f'SELECT * FROM {table}'
    return statement


def query_data(database, query):
    return


def insert_data(database, statement, values):
    return


def update_data(database, statement, values):
    return


def remove_data(database, statement):
    return


def dict_to_sqlite(database, headers, dictionary):
    return status


def sqlite_to_dict(database, headers):
    return dictionary


def dict_to_postgre(database, headers, dictionary):
    return status


def postgre_to_dict(database, headers):
    return dictionary


def json_to_sqlite(database, headers, values):
    return status


def sqlite_to_json(database, headers):
    return java


def json_to_postgre(database, headers, values):
    return status


def postgre_to_json(database, headers):
    return java



