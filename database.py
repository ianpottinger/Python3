#! /usr/bin/env python3		#Allow Unix shell to execute as a Python script
# _*_ coding: UTF-8 _*_		#Enable unicode encoding
#GMT+0BST-1,M3.5.0/01:00:00,M10.5.0/02:00:00

__author__ = "Ian Pottinger"
__date__ = "20/12/2012"
__contact__ = "ianpottinger@me.com"
__version__ = "1.3.5.7.9 even avoidance"
__credits__ = "Commonly known as Potts"
__copyright__ = "Copyleft for balance"
__license__ = "Whatever Potts Decides"
__metadata__ = [__author__, __date__, __contact__, __version__,
                __credits__, __copyright__, __license__]


import multiprocessing
import concurrent
import threading
import asyncio
import doctest
import sqlite3
import psycopg2
import pymongo
import mongoengine
import mariadb
import keyword
import unittest

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
>>> database, cursor = connect_database('sqlite', 'sqlite.sl3')
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
    """
#>>> memory, cursor = restore_sqlite3_memory('sqlite.sl3', ':memory:')
    """

    def indicator(status, remaining, total):
        print(f'{total - remaining} of {total} pages completed.')

    archive = sqlite3.connect(source)
    restore = sqlite3.connect(destination)
    archive.backup(restore, pages = 1, progress = indicator)
    restore.commit()
    return restore, restore.cursor()


def dump_sqlite3_datafile(source = 'sqlite.sl3', destination = 'memory.sl3'):
    """
>>> memory, cursor = connect_database('sqlite', ':memory:')
>>> sqlite3_file = dump_sqlite3_datafile(':memory:', 'sqlite.sl3')
>>> print(sqlite3_file)
<_io.TextIOWrapper name='sqlite.sl3' mode='w' encoding='cp1252'>
    """
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
    """
>>> database, cursor = connect_database('sqlite', ':memory:')
>>> cursor = create_table(cursor, 'Hash', 'Pair_Id data_type PRIMARY KEY, Key data_type NOT NULL UNIQUE, Value data_type NOT NULL')
Executing SQL:
CREATE TABLE IF NOT EXISTS Hash (Pair_Id data_type PRIMARY KEY, Key data_type NOT NULL UNIQUE, Value data_type NOT NULL);
<BLANKLINE>
    """

    statement = f'CREATE TABLE IF NOT EXISTS {table_name} ({table_columns});'
    print(f'Executing SQL:\n{statement}\n')
    cursor.execute(statement)
    return cursor


def drop_table(cursor, table_name):
    """
>>> database, cursor = connect_database('sqlite', ':memory:')
>>> cursor = create_table(cursor, 'Hash', 'Pair_Id data_type PRIMARY KEY, Key data_type NOT NULL UNIQUE, Value data_type NOT NULL')
Executing SQL:
CREATE TABLE IF NOT EXISTS Hash (Pair_Id data_type PRIMARY KEY, Key data_type NOT NULL UNIQUE, Value data_type NOT NULL);
<BLANKLINE>
>>> cursor = drop_table(cursor, 'Hash')
Executing SQL:
DROP TABLE IF EXISTS Hash;
<BLANKLINE>
    """

    statement = f'DROP TABLE IF EXISTS {table_name};'
    print(f'Executing SQL:\n{statement}\n')
    cursor.execute(statement)
    return cursor


def return_table(cursor, table_name):
    """
>>> database, cursor = connect_database('sqlite', ':memory:')
>>> cursor = create_table(cursor, 'Hash', 'Pair_Id data_type PRIMARY KEY, Key data_type NOT NULL UNIQUE, Value data_type NOT NULL')
Executing SQL:
CREATE TABLE IF NOT EXISTS Hash (Pair_Id data_type PRIMARY KEY, Key data_type NOT NULL UNIQUE, Value data_type NOT NULL);
<BLANKLINE>
>>> return_table(cursor, 'Hash')
Executing SQL:
SELECT * FROM Hash;
<BLANKLINE>
    """

    statement = f'SELECT * FROM {table_name};'
    print(f'Executing SQL:\n{statement}\n')
    #table = cursor.execute(statement)
    #print(cursor.fetchall())
    for row in cursor.execute(statement):
        print(row)
    return


def where_group_order(statement, expression = "", ordering = "", grouping = ""):
    modifiers = ""
    if not(expression == ""):
        modifiers += f"\nWHERE {expression}"
    if not(ordering == ""):
        modifiers += f"\nORDER BY {ordering}"
    if not(grouping == ""):
        modifiers += f"\nGROUP BY {grouping}"
    statement += modifiers
    return statement


def return_sorted(cursor, table_name, column, query,
                  columns = '*', order = 'DESC'):
    """
>>> database, cursor = connect_database('sqlite', ':memory:')
>>> cursor = create_table(cursor, 'Hash', 'Pair_Id, Key, Value')
Executing SQL:
CREATE TABLE IF NOT EXISTS Hash (Pair_Id, Key, Value);
<BLANKLINE>
>>> insert_rows(cursor, 'Hash', 'Pair_Id, Key, Value', ['1, "Username", "Password"', '2, "Longitude", "Latitude"'])
?,?,?
Executing SQL:
INSERT INTO Hash (Pair_Id, Key, Value) VALUES (?,?,?); on ['1, "Username", "Password"', '2, "Longitude", "Latitude"']
<BLANKLINE>
Executing SQL:
SELECT * FROM Hash;
<BLANKLINE>
(1, 'Username', 'Password')
(2, 'Longitude', 'Latitude')
>>> cursor = return_sorted(cursor, 'Hash', 'Value', 'Key', order = '')
Executing SQL:
SELECT *
FROM Hash
ORDER BY Value ;
<BLANKLINE>
(2, 'Longitude', 'Latitude')
(1, 'Username', 'Password')

    """

    statement = f'SELECT {columns}\nFROM {table_name}\nORDER BY {column} {order};'
    print(f'Executing SQL:\n{statement}\n')
    for row in cursor.execute(statement):
        print(row)
    return


def count_rows(cursor, table_name):
    """
>>> database, cursor = connect_database('sqlite', ':memory:')
>>> cursor = create_table(cursor, 'Hash', 'Pair_Id, Key, Value')
Executing SQL:
CREATE TABLE IF NOT EXISTS Hash (Pair_Id, Key, Value);
<BLANKLINE>
>>> insert_rows(cursor, 'Hash', 'Pair_Id, Key, Value', ['1, "Username", "Password"', '2, "Longitude", "Latitude"', '3, "Object", "Physical"', '4, "Subject", "Construct"'])
?,?,?
Executing SQL:
INSERT INTO Hash (Pair_Id, Key, Value) VALUES (?,?,?); on ['1, "Username", "Password"', '2, "Longitude", "Latitude"', '3, "Object", "Physical"', '4, "Subject", "Construct"']
<BLANKLINE>
Executing SQL:
SELECT * FROM Hash;
<BLANKLINE>
(1, 'Username', 'Password')
(2, 'Longitude', 'Latitude')
(3, 'Object', 'Physical')
(4, 'Subject', 'Construct')
>>> count_rows(cursor, 'Hash')
Executing SQL:
SELECT COUNT(*) FROM Hash;
<BLANKLINE>
[(4,)]
    """

    statement = f'SELECT COUNT(*) FROM {table_name};'
    print(f'Executing SQL:\n{statement}\n')
    cursor.execute(statement)
    return cursor.fetchall()


def column_range(cursor, table_name, column):
    """
>>> database, cursor = connect_database('sqlite', ':memory:')
>>> cursor = create_table(cursor, 'Hash', 'Pair_Id, Key, Value')
Executing SQL:
CREATE TABLE IF NOT EXISTS Hash (Pair_Id, Key, Value);
<BLANKLINE>
>>> insert_rows(cursor, 'Hash', 'Pair_Id, Key, Value', ['1, "Username", "Password"', '2, "Longitude", "Latitude"', '3, "Object", "Physical"', '4, "Subject", "Construct"'])
?,?,?
Executing SQL:
INSERT INTO Hash (Pair_Id, Key, Value) VALUES (?,?,?); on ['1, "Username", "Password"', '2, "Longitude", "Latitude"', '3, "Object", "Physical"', '4, "Subject", "Construct"']
<BLANKLINE>
Executing SQL:
SELECT * FROM Hash;
<BLANKLINE>
(1, 'Username', 'Password')
(2, 'Longitude', 'Latitude')
(3, 'Object', 'Physical')
(4, 'Subject', 'Construct')
>>> column_range(cursor, 'Hash', 'Pair_Id')
Executing SQL:
SELECT MIN(Pair_Id), MAX(Pair_Id) FROM Hash;
<BLANKLINE>
[(1, 4)]
    """

    statement = f'SELECT MIN({column}), MAX({column}) FROM {table_name};'
    print(f'Executing SQL:\n{statement}\n')
    cursor.execute(statement)
    return cursor.fetchall()


def group_average(cursor, table_name, grouping, values):
    """
#>>> database, cursor = connect_database('sqlite', ':memory:')
#>>> cursor = create_table(cursor, 'Hash', 'Pair_Id, Key, Value')
Executing SQL:
CREATE TABLE IF NOT EXISTS Hash (Pair_Id, Key, Value);
<BLANKLINE>
#>>> insert_rows(cursor, 'Hash', 'Pair_Id, Key, Value', ['1, "Username", "Password"', '2, "Longitude", "Latitude"', '3, "Object", "Physical"', '4, "Subject", "Construct"'])
?,?,?
Executing SQL:
INSERT INTO Hash (Pair_Id, Key, Value) VALUES (?,?,?); on ['1, "Username", "Password"', '2, "Longitude", "Latitude"', '3, "Object", "Physical"', '4, "Subject", "Construct"']
<BLANKLINE>
Executing SQL:
SELECT * FROM Hash;
<BLANKLINE>
(1, 'Username', 'Password')
(2, 'Longitude', 'Latitude')
(3, 'Object', 'Physical')
(4, 'Subject', 'Construct')
#>>> group_average(cursor, 'Hash', 'Year', 'Event')
Executing SQL:
SELECT Year, AVG(Event) FROM Hash GROUP BY Year ORDER BY Year;
<BLANKLINE>
    """

    statement = f'SELECT {grouping}, AVG({values}) FROM {table_name} GROUP BY {grouping} ORDER BY {grouping};'
    print(f'Executing SQL:\n{statement}\n')
    cursor.execute(statement)
    return cursor.fetchall()



def distinct_values(cursor, table_name, column):
    """
>>> database, cursor = connect_database('sqlite', ':memory:')
>>> cursor = create_table(cursor, 'Hash', 'Pair_Id, Key, Value')
Executing SQL:
CREATE TABLE IF NOT EXISTS Hash (Pair_Id, Key, Value);
<BLANKLINE>
>>> insert_rows(cursor, 'Hash', 'Pair_Id, Key, Value', ['1, "Username", "Password"', '2, "Longitude", "Latitude"', '3, "Object", "Physical"', '4, "Subject", "Construct"'])
?,?,?
Executing SQL:
INSERT INTO Hash (Pair_Id, Key, Value) VALUES (?,?,?); on ['1, "Username", "Password"', '2, "Longitude", "Latitude"', '3, "Object", "Physical"', '4, "Subject", "Construct"']
<BLANKLINE>
Executing SQL:
SELECT * FROM Hash;
<BLANKLINE>
(1, 'Username', 'Password')
(2, 'Longitude', 'Latitude')
(3, 'Object', 'Physical')
(4, 'Subject', 'Construct')
>>> distinct_values(cursor, 'Hash', 'Value')
Executing SQL:
SELECT DISTINCT Value FROM Hash ORDER BY Value;
<BLANKLINE>
[('Construct',), ('Latitude',), ('Password',), ('Physical',)]
    """

    statement = f'SELECT DISTINCT {column} FROM {table_name} ORDER BY {column};'
    print(f'Executing SQL:\n{statement}\n')
    cursor.execute(statement)
    return cursor.fetchall()


def query_rows(cursor, table_name, column, query, columns = '*'):
    entry = (f'{query}',)
    statement = f'SELECT {columns} FROM {table_name} WHERE {column} = ?;'
    print(f'Executing SQL:\n{statement} for {entry}')
    result = cursor.execute(statement, entry)
    #print(cursor.fetchall())
    return (cursor.fetchall())


def union_query(cursor, m_table_name, m_column, m_query, m_columns,
                s_table_name, s_column, s_query, s_columns):
    statement = f'SELECT {m_columns}\nFROM {m_table_name}\nWHERE {m_column} = {m_query}\nUNION\nSELECT {s_columns}\nFROM {s_table_name}\nWHERE {s_column} = {s_query};'
    print(f'Executing SQL:\n{statement}')
    result = cursor.execute(statement, entry)
    #print(cursor.fetchall())
    return (cursor.fetchall())


def create_view(cursor, view_name, table_name, column, query, columns = '*'):
    entry = (f'{query}',)
    statement = f'CREATE VIEW {view_name} AS SELECT {columns} FROM {table_name} WHERE {column} = ?;'
    print(f'Executing SQL:\n{statement} for {entry}')
    result = cursor.execute(statement, entry)
    #print(cursor.fetchall())
    return (cursor.fetchall())


def insert_rows(cursor, table_name, columns, values_list):
    """
>>> database, cursor = connect_database('sqlite', ':memory:')
>>> cursor = create_table(cursor, 'Hash', 'Pair_Id, Key, Value')
Executing SQL:
CREATE TABLE IF NOT EXISTS Hash (Pair_Id, Key, Value);
<BLANKLINE>
>>> insert_rows(cursor, 'Hash', 'Pair_Id, Key, Value', ['1, "Username", "Password"', '2, "Longitude", "Latitude"'])
?,?,?
Executing SQL:
INSERT INTO Hash (Pair_Id, Key, Value) VALUES (?,?,?); on ['1, "Username", "Password"', '2, "Longitude", "Latitude"']
<BLANKLINE>
Executing SQL:
SELECT * FROM Hash;
<BLANKLINE>
(1, 'Username', 'Password')
(2, 'Longitude', 'Latitude')
>>> cursor = return_table(cursor, 'Hash')
Executing SQL:
SELECT * FROM Hash;
<BLANKLINE>
(1, 'Username', 'Password')
(2, 'Longitude', 'Latitude')
    """

    headers = len(columns.split(',')) - 1
    elements = '?'
    for element in range(headers):
        elements += ',?'
    print(elements)

    secure_statement = f'INSERT INTO {table_name} ({columns}) VALUES ({elements});'
    print(f'Executing SQL:\n{secure_statement} on {values_list}\n')
    for values in values_list:
        statement = f'INSERT INTO {table_name} ({columns}) VALUES ({values});\n'
        cursor.execute(statement)
    return return_table(cursor, table_name)


def update_rows(cursor, table_name, column, value, search, query):
    """
>>> database, cursor = connect_database('sqlite', ':memory:')
>>> cursor = create_table(cursor, 'Hash', 'Pair_Id, Key, Value')
Executing SQL:
CREATE TABLE IF NOT EXISTS Hash (Pair_Id, Key, Value);
<BLANKLINE>
>>> insert_rows(cursor, 'Hash', 'Pair_Id, Key, Value', ['1, "Username", "Password"', '2, "Longitude", "Latitude"'])
?,?,?
Executing SQL:
INSERT INTO Hash (Pair_Id, Key, Value) VALUES (?,?,?); on ['1, "Username", "Password"', '2, "Longitude", "Latitude"']
<BLANKLINE>
Executing SQL:
SELECT * FROM Hash;
<BLANKLINE>
(1, 'Username', 'Password')
(2, 'Longitude', 'Latitude')
>>> return_table(cursor, 'Hash')
Executing SQL:
SELECT * FROM Hash;
<BLANKLINE>
(1, 'Username', 'Password')
(2, 'Longitude', 'Latitude')
>>> update_rows(cursor, 'Hash', 'Value', '"Location"', 'Key', '"Username"')
Executing SQL:
UPDATE Hash SET Value = "Location" WHERE Key = "Username";
<BLANKLINE>
to update Value column in Hash table
where Key column matches condition for "Username" row.
Executing SQL:
SELECT * FROM Hash;
<BLANKLINE>
(1, 'Username', 'Location')
(2, 'Longitude', 'Latitude')
    """

    statement = f'UPDATE {table_name} SET {column} = {value} WHERE {search} = {query};'
    print(f'Executing SQL:\n{statement}\n')
    print(f'to update {column} column in {table_name} table')
    print(f'where {search} column matches condition for {query} row.')
    cursor.execute(statement)
    return return_table(cursor, table_name)


def update_column_rows(cursor, table_name, columns, values, searches, queries,
                       logic = 'AND'):
    """
>>> database, cursor = connect_database('sqlite', ':memory:')
>>> cursor = create_table(cursor, 'Hash', 'Pair_Id, Key, Value')
Executing SQL:
CREATE TABLE IF NOT EXISTS Hash (Pair_Id, Key, Value);
<BLANKLINE>
>>> insert_rows(cursor, 'Hash', 'Pair_Id, Key, Value', ['1, "Username", "Password"', '2, "Longitude", "Latitude"', '3, "Object", "Physical"', '4, "Subject", "Construct"'])
?,?,?
Executing SQL:
INSERT INTO Hash (Pair_Id, Key, Value) VALUES (?,?,?); on ['1, "Username", "Password"', '2, "Longitude", "Latitude"', '3, "Object", "Physical"', '4, "Subject", "Construct"']
<BLANKLINE>
Executing SQL:
SELECT * FROM Hash;
<BLANKLINE>
(1, 'Username', 'Password')
(2, 'Longitude', 'Latitude')
(3, 'Object', 'Physical')
(4, 'Subject', 'Construct')
>>> update_column_rows(cursor, 'Hash', 'Value,Value', '"Location","Questionable"', 'Key,Key', '"Username","Subject"', logic = 'OR')
    """

    headers = len(columns.split(',')) - 1
    elements = '?'
    for element in range(headers):
        elements += ',?'
    print(elements)
    secure_statement = f'UPDATE {table_name} ({columns}) VALUES ({elements});'

    if str(type(columns)) == "<class 'str'>":
        columns = columns.split(",")
    if str(type(values)) == "<class 'str'>":
        values = values.split(",")
    print(columns, values)
    elements = f'{columns[0]} = {values[0]}'
    for element in range(headers):
        elements += f', {columns[element + 1]} = {values[element + 1]}'
    print(f"Elements: {elements}")

    if str(type(searches)) == "<class 'str'>":
        searches = searches.split(",")
    if str(type(queries)) == "<class 'str'>":
        queries = queries.split(",")
    print(searches, queries)
    conditions = len(searches) - 1
    expressions = f'{searches[0]} = {queries[0]}'
    for expression in range(conditions):
        expressions += f' {logic} {searches[expression + 1]} = {queries[expression + 1]}'
    print(f"Expressions: {expressions}")

    statement = f'UPDATE {table_name} SET {elements} WHERE {expressions};'
    print(f'Executing SQL:\n{statement}\n')
    print(f'to update {columns} column/s with {values} value/s')
    print(f'in {table_name} table')
    print(f'where {searches} column row/s match condition/s for {queries}')
    cursor.execute(statement) #, columns, values, searches, queries)
    return return_table(cursor, table_name)


def remove_rows(cursor, table_name, searches, queries, logic = 'OR'):
    """
>>> database, cursor = connect_database('sqlite', ':memory:')
>>> cursor = create_table(cursor, 'Hash', 'Pair_Id, Key, Value')
Executing SQL:
CREATE TABLE IF NOT EXISTS Hash (Pair_Id, Key, Value);
<BLANKLINE>
>>> insert_rows(cursor, 'Hash', 'Pair_Id, Key, Value', ['1, "Username", "Password"', '2, "Longitude", "Latitude"', '3, "Object", "Physical"', '4, "Subject", "Construct"'])
?,?,?
Executing SQL:
INSERT INTO Hash (Pair_Id, Key, Value) VALUES (?,?,?); on ['1, "Username", "Password"', '2, "Longitude", "Latitude"', '3, "Object", "Physical"', '4, "Subject", "Construct"']
<BLANKLINE>
Executing SQL:
SELECT * FROM Hash;
<BLANKLINE>
(1, 'Username', 'Password')
(2, 'Longitude', 'Latitude')
(3, 'Object', 'Physical')
(4, 'Subject', 'Construct')
>>> remove_rows(cursor, 'Hash', 'Key,Key', '"Username","Subject"')
?,?
['Key', 'Key'] ['"Username"', '"Subject"']
Expressions: Key = "Username" OR Key = "Subject"
Executing SQL:
DELETE FROM Hash WHERE Key = "Username" OR Key = "Subject";
<BLANKLINE>
to remove rows/s in Hash table
where ['Key', 'Key'] column row/s match condition/s for ['"Username"', '"Subject"']
Executing SQL:
SELECT * FROM Hash;
<BLANKLINE>
(2, 'Longitude', 'Latitude')
(3, 'Object', 'Physical')
    """

    headers = len(searches.split(',')) - 1
    elements = '?'
    for element in range(headers):
        elements += ',?'
    print(elements)
    secure_statement = f'DELETE FROM {table_name} WHERE {elements};'

    if str(type(searches)) == "<class 'str'>":
        searches = searches.split(",")
    if str(type(queries)) == "<class 'str'>":
        queries = queries.split(",")
    print(searches, queries)
    conditions = len(searches) - 1
    expressions = f'{searches[0]} = {queries[0]}'
    for expression in range(conditions):
        expressions += f' {logic} {searches[expression + 1]} = {queries[expression + 1]}'
    print(f"Expressions: {expressions}")

    statement = f'DELETE FROM {table_name} WHERE {expressions};'
    print(f'Executing SQL:\n{statement}\n')
    print(f'to remove rows/s in {table_name} table')
    print(f'where {searches} column row/s match condition/s for {queries}')
    cursor.execute(statement) #, searches, queries)
    return return_table(cursor, table_name)


def join_tables(cursor, left_table, right_table, left_column, right_column,
                expression = "", ordering = "", grouping = "",
                columns = '*', join_type = 'INNER'):
    if (join_type.upper()) in ['INNER', 'LEFT', 'RIGHT', 'FULL']:
        join_type = join_type.upper()
    #if  engine == 'sqlite' and join_type == 'FULL':
    #    print('FULL join unsupported by SQLite3. Returning INNER join only.')
    #    join_type = 'INNER'

    statement = f'SELECT {columns}\nFROM {left_table}\n{join_type} {right_table} ON {left_table}.{left_column} = {right_table}.{right_column}'
    statement = where_group_order(statement, expression, ordering, grouping)
    print(f'Executing SQL:\n{statement}\n')
    print(f'to {join_type.lower()} join {left_table}.{left_column} with {right_table}.{right_column}')
    #cursor.execute(statement)
    return


def create_index(cursor, table_name, index_name, columns):

    statement = f'CREATE INDEX {index_name} ON table_name ({colums})'
    print(f'Executing SQL:\n{statement}\n')
    print(f'to create an index named {index_name} for table {table_name} using column/s {columns}')
    #cursor.execute(statement)
    return


def cross_join():
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

if __name__ == '__main__':
    doctest.testmod()
    unittest.main(exit=False)
