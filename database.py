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
    sqlite3.enable_callback_tracebacks(DEBUG_MODE)
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

# https://docs.python.org/3/library/sqlite3.html
ACID = ['Atomicity', 'Consistency', 'Isolation', 'Durability']


def connect_database(engine, filename = ':memory:'):
    """
>>> database, cursor = connect_database('sqlite')
    """
    if engine == "sqlite":
        database = sqlite3.connect(filename)
        database.enable_load_extension(True)
        #database.execute("SELECT load_extension('./fts3.so')")
        #database.load_extension('./fts3.so') #SQLite3 Full text search
        database.enable_load_extension(False)
    elif engine == "postgre":
        if filename == ':memory:':
            return 'Memory resident database not support with PostgreSQL'
    else:
        return 'Unsupported engine. Options are sqlite or postgre'
    return database, database.cursor()


def create_database(filepath, filename):
    database = filepath + filename
    return


def dump_sqlite3_memory(database, destination = 'memory.sl3'):
    with open(destination, 'w') as sqlite3_file:
        for row in database.iterdump():
            sqlite3_file.write('%s\n' % row)
    return sqlite3_file


def restore_sqlite3_memory(source = 'memory.sl3', destination = ':memory:'):
    def indicator(status, remaining, total):
        print(f'{total - remaining} of {total} pages completed.')
    archive = sqlite3.connect(source)
    restore = sqlite3.connect(destination)
    archive.backup(restore, pages = 1, progress = indicator)
    return restore


def dump_sqlite3_datafile(source = ':memory:', destination = 'memory.sl3'):
    database = sqlite3.connect(source)
    with open(destination, 'w') as sqlite3_file:
        for row in database.iterdump():
            sqlite3_file.write('%s\n' % row)
    return sqlite3_file


def drop_database(database):
    database.total_changes
    database.drop()
    return


def close_database(database):
    database.commit()
    database.total_changes
    database.close()
    return


def close_cursor(cursor):
    database = cursor.connection()
    cursor.close()
    return database


def create_table(cursor, table_name, table_columns):
    statement = f'CREATE TABLE {table_name} ({table_columns})'
    print(f'Executing: {statement}')
    cursor.execute(statement)
    return cursor


def drop_table(cursor, table_name):
    statement = f'DROP TABLE {table_name}'
    print(f'Executing: {statement}')
    cursor.execute(statement)
    return cursor


def return_table(cursor, table_name):
    statement = f'SELECT * FROM {table_name}'
    print(f'Executing: {statement}')
    table = cursor.execute(statement)
    print(cursor.fetchall())
    return


def return_sorted(cursor, table_name, column, query,
                  columns = '*', order = 'ASEC'):
    statement = f'SELECT {columns} FROM {table_name} ORDER BY {column} {order}'
    print(f'Executing: {statement}')
    for row in cursor.execute(statement):
        print(row)
    return


def query_data(cursor, table_name, column, query, columns = '*'):
    entry = (f'{query}',)
    statement = f'SELECT {columns} FROM {table_name} WHERE {column} = ?'
    print(f'Executing: {statement} for {entry}')
    result = cursor.execute(statement, entry)
    print(cursor.fetchall())
    return


def insert_data(cursor, table_name, values):
    columns = len(values[0]) - 1
    elements = '?'
    for element in range(columns):
        elements += ',?'
    statement = f'INSERT INTO {table_name} VALUES ({elements})'
    print(f'Executing: {statement} on {values}')
    cursor.executemany(statement, values)
    return return_table(cursor, table_name)


def update_data(cursor, statement, values):
    return


def remove_data(cursor, statement):
    return


def dict_to_sqlite(cursor, headers, dictionary):
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


def sqlite3_shell():
    con = sqlite3.connect(":memory:")
    con.isolation_level = None
    cur = con.cursor()

    buffer = ""

    print("Enter your SQL commands to execute in sqlite3.")
    print("Enter a blank line to exit.")

    while True:
        line = input()
        if line == "":
            break
        buffer += line
        if sqlite3.complete_statement(buffer):
            try:
                buffer = buffer.strip()
                cur.execute(buffer)

                if buffer.lstrip().upper().startswith("SELECT"):
                    print(cur.fetchall())
            except sqlite3.Error as e:
                print("An error occurred:", e.args[0])
            buffer = ""

    con.close()
    return



print(sqlite3.version, sqlite3.version_info, sqlite3.sqlite_version, sqlite3.sqlite_version_info)

