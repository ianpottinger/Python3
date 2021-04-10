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


import smtplib
import datetime
import itertools
import doctest
import keyword
import re
import struct
import unittest
import uuid
import maths
import random
import win32com.client as wincl
import multiprocessing
import concurrent
import threading
import asyncio

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

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

relay = smtplib.SMTP('smtp.google.com', 25)
relay.ehlo()

with open('password.key', 'r') as secret:
    password = secret.read
relay.login('username@mail.com', password)

message = MIMEMultipart()
message['From'] = 'username@mail.com'
message['To'] = 'spamhere@dumpnull'
message['Subject'] = 'Test'

with open('content.msg', 'r') as body:
    content = body.read
message.attach(MIMEText(content, 'plain'))

filename = 'image.png'
attachment = open(filename, 'rb')
payload = MIMEBase('application', 'actet-stream')
payload.set_payload(attachment.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', f'attachment; filename={filename}')
message.attach(payload)

package = message.as_string()
relay.sendmail(message['From'], 'message['To']', package)
