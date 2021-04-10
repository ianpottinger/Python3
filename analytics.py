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


import pandas as pd
import pandas_profiling

#df = pd.read_csv("G:\WorkingData\Work @ Home\Insecurity\Approved-Gaming-Media-List-1-1-1.csv")
#pandas_profiling.ProfileReport(df).to_file("G:\WorkingData\Work @ Home\Insecurity\ProfileReport.html")



from pivottablejs import pivot_ui

#df = pd.read_csv("G:\WorkingData\Work @ Home\Insecurity\Approved-Gaming-Media-List-1-1-1.csv")
#pivot_ui(df)



from pydqc.data_compare import distribution_compare_pretty

#train = pd.read_csv("G:\WorkingData\Work @ Home\Insecurity\Approved-Gaming-Media-List-1-1-1.csv")
#test = pd.read_csv("G:\WorkingData\Work @ Home\Insecurity\Approved-Gaming-Media-List-1-1-1.csv")
#distribution_compare_pretty(train, test, "SOME COLUMNS", figsize=None)



import multiprocessing
import concurrent
import threading
import asyncio
import pandas
import sklearn
import tensorflow as tf
from tensorflow import keras
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


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
