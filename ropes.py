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
import queue, heapq, collections, pickle
import threading, concurrent, subprocess
import numbers, operator, math, cmath, decimal, fractions, random
import itertools, functools
import string, textwrap, re, unicodedata, locale, uuid, binascii
import doctest, unittest, cProfile, timeit, logging, traceback, pdb
import ipaddress, socket, email, html
import ftplib, poplib, nntplib, smtplib, telnetlib, urllib, hashlib, zlib
import argparse, datetime, calendar, pprint, struct, copy
import shutil, tempfile, glob
import tkinter, colorama, turtle  # , dateutil, numpy, scipy, pygame, matplotlib, pygobject

DEBUG_MODE = False
if DEBUG_MODE:
    pdb.set_trace()

RESERVED = ["and", "del", "from", "not", "while", "as", "elif",
            "global", "or", "with", "assert", "else", "if", "pass",
            "yield", "break", "except", "import", "print", "class",
            "exec", "in", "raise", "continue", "finally", "is",
            "return", "def", "for", "lambda", "try"]
KEYWORDS = keyword.kwlist

GLOBAL_SONG = r"Supercalifragilisticexpialidocious"
GLOBAL_LONG_WORD_FEAR = r"hippopotomonstrosesquippedaliophobia"
GLOBAL_PANGRAM = r"The quick brown fox jumps over the lazy dog"
GLOBAL_ANAGRAM1 = r"TWELVE PLUS ONE"
GLOBAL_ANAGRAM2 = r"ELEVEN PLUS TWO"
GLOBAL_SPELLS = ['Abra Cadabra', 'Hocus Pocus', 'Open Sesame', 'Hey Presto']
GLOBAL_FLIP = "neveroddoreven"

GLOBAL_HILL = "Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu"
GLOBAL_HILL_ENG = "The summit where Tamatea, the man with the big knees, the climber of mountains, the land-swallower who travelled about, played his nose flute to his loved one"
GLOBAL_TOWN = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
GLOBAL_TOWN_ENG = "The church of St. Mary in a hollow of white hazel near the rapid whirlpool and St. Tysilio's church of the red cave."
GLOBAL_LAKE = "Chargoggagoggmanchauggagoggchaubunagungamaugg"
GLOBAL_LAAKE_ENG = "Fishing Place at the Boundaries -- Neutral Meeting Grounds"
GLOBAL_FARM = "Tweebuffelsmeteenskootmorsdoodgeskietfontein"
GLOBAL_FARM_ENG = "The spring where two buffaloes were cleanly killed with a single shot"

TUQoLtUaE = r"""
Without the groundation of darkness, gnosis cannot lead to enlightenment;
From the calm of the ether, came the expression of our consciousness;
The natural balance of our universe from the laws of ordered chaos;
An everliving cyclic transition of energy between states of intent;
Smai Tawi of scared feminine principles with divine masculine actions;
Interdependence between our unique spiritual and tangible matters of life;
Humanity reaching the euphoria of truth within a fabric of vibrational desires.
"""

binINbin = """01001000 01100101 01101100 01101100 01101111 01111110 00100001 00100000 00110000 00110001 00110000 00110000 00110001 00110001 00110000 00110000 00100000 00110000 00110001 00110001 00110000 00110001 00110001 00110001 00110001 00100000 00110000 00110001 00110001 00110001 00110000 00110001 00110001 00110000 00100000 00110000 00110001 00110001 00110000 00110000 00110001 00110000 00110001 00100000 00110000 00110000 00110001 00110000 00110000 00110000 00110000 00110000 00100000 00110000 00110001 00110001 00110001 00110001 00110000 00110000 00110001 00100000 00110000 00110001 00110001 00110000 00110001 00110001 00110001 00110001 00100000 00110000 00110001 00110001 00110001 00110000 00110001 00110000 00110001 00100000 00110000 00110000 00110001 00110000 00110000 00110000 00110000 00110000 00100000 00110000 00110001 00110001 00110000 00110000 00110000 00110000 00110001 00100000 00110000 00110001 00110001 00110000 00110001 00110001 00110000 00110000 00100000 00110000 00110001 00110001 00110000 00110001 00110001 00110000 00110000 00100000 00110000 00110000 00110001 00110000 00110000 00110000 00110000 00110001 00100000"""

GLOBAL_EN_VOWELS = "AEIOUaeiou"
QWERTY_UK = "1234567890qwertyuiopasdfghjklzxcvbnm"
ALPHABET_LOWER = "abcdefghijklmnopqrstuvwxyz"  # ASCII 97 - 122
ALPHABET_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # ASCII 65 - 90
ASCII_CHARACTERS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""  # note the space at the front
REGEX_DIGITS = "\D"
REGEX_LETTERS = "[^A-Za-z]"
UNICODE_STRING = u"UniCode string"
KEY_MAP = {'back space': 8, 'tab': 9,
           'enter': 13, 'shift': 16, 'ctrl': 17,
           'break': 19, 'caps': 20, 'escape': 27,
           ' ': 32, 'space': 32,
           'page up': 33, 'page down': 34, 'end': 35, 'home': 36,
           'left': 37, 'up': 38, 'right': 39, 'down': 40,
           'print': 44, 'insert': 45, 'delete': 46,
           '0': 48, '1': 49, '2': 50, '3': 51, '4': 52,
           '5': 53, '6': 54, '7': 55, '8': 56, '9': 57,
           'a': 65, 'A': 65, 'b': 66, 'B': 66,
           'c': 67, 'C': 67, 'd': 68, 'D': 68,
           'e': 69, 'E': 69, 'f': 70, 'F': 70,
           'g': 71, 'G': 71, 'h': 72, 'H': 72,
           'i': 73, 'I': 73, 'j': 74, 'J': 74,
           'k': 75, 'K': 75, 'l': 76, 'L': 76,
           'm': 77, 'M': 77, 'n': 78, 'N': 78,
           'o': 79, 'O': 79, 'p': 80, 'P': 80,
           'q': 81, 'Q': 81, 'r': 82, 'R': 82,
           's': 83, 'S': 83, 't': 84, 'T': 84,
           'u': 85, 'U': 85, 'v': 86, 'V': 86,
           'w': 87, 'W': 87, 'x': 88, 'X': 88,
           'y': 89, 'Y': 89, 'z': 90, 'Z': 90,
           '*': 106, '+': 107, '-': 109, '-': 189,
           '.': 110, '.': 190, '/': 111, '/': 191,
           'nums': 144, 'scroll': 145,
           '=': 187, ',': 188, '\\': 220, '`': 223}

MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
              'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..',
              'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '----',
              '1': '.---', '2': '..---', '3': '...--',
              '4': '...-', '5': '....', '6': '-...',
              '7': '--...', '8': '---..', '9': '---..',
              '.': '.-.-.-', ',': '--..--', '?': '..--..',
              "'": '.----.', '!': '-.-.--', '/': '-..-.',
              '(': '-.--.', ')': '-.--.-', '&': '.-...',
              ':': '-.-.-.', '=': '-...-', '+': '.-.-.',
              '-': '-....-', '_': '..--.-', '"': '.-..-.',
              '$': '...-..-', '@': '.--.-.', 'start': '-.-.-',
              'invite': '-.-', 'ack': '...-.', 'error': '........',
              'end': '...-.-'}

PHONIC_CODE = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie',
               'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
               'G': 'Golf', 'H': 'Hotel', 'I': 'India',
               'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
               'M': 'Mike', 'N': 'November', 'O': 'Oscar',
               'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
               'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
               'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
               'Y': 'Yankee', 'Z': 'Zulu', '0': 'Zero',
               '1': 'One', '2': 'Two', '3': 'Three',
               '4': 'Four', '5': 'Five', '6': 'Six',
               '7': 'Seven', '8': 'Eight', '9': 'Nine'}

SPELL_LETTERS = {"A": "ay", "B": "bee", "C": "cee", "D": "dee",
                 "E": "eee", "F": "eff", "G": "gee", "H": "aych",
                 "I": "eye", "J": "jay", "K": "kay", "L": "elle",
                 "M": "em", "N": "en", "O": "oh", "P": "pee",
                 "Q": "cue", "R": "are", "S": "ess", "T": "tee",
                 "U": "you", "V": "vee", "W": "dubbayou",
                 "X": "ex", "Y": "why", "Z": "zee"}

FLIP_TABLE = {"a": "\u0250", "b": "q", "c": "\u0254", "d": "p",
              "e": "\u01DD", "f": "\u025F", "g": "\u0183", "h": "\u0265",
              "i": "\u0131", "j": "\u027E", "k": "\u029E", "l": "|",
              "m": "\u026F", "n": "u", "o": "o", "p": "d",
              "q": "b", "r": "\u0279", "s": "s", "t": "\u0287",
              "u": "n", "v": "\u028C", "w": "\u028D", "x": "x",
              "y": "\u028E", "z": "z", "A": "\u0250", "B": "q",
              "C": "\u0254", "D": "p", "E": "\u01DD", "F": "\u025F",
              "G": "\u0183", "H": "\u0265", "I": "\u0131", "J": "\u027E",
              "K": "\u029E", "L": "|", "M": "\u026F", "N": "u",
              "O": "o", "P": "d", "Q": "b", "R": "\u0279",
              "S": "s", "T": "\u0287", "U": "n", "V": "\u028C",
              "W": "\u028D", "X": "x", "Y": "\u028E", "Z": "z",
              ".": "\u02D9", "[": "]", "'": ",", ",": "'",
              "(": ")", "{": "}", "?": "\u00BF", "!": "\u00A1",
              "\"": ",", "<": ">", "_": "\u203E", ";": "\u061B",
              "\u203F": "\u2040", "\u2045": "\u2046", "\u2234": "\u2235",
              "\r": "\n", " ": " "}

HTML_RESERVE = {'"': '&quot;', "'": '&apos;', '&': '&amp;', '<': '&lt;', '>': '&gt;'}
URL_ENCODE = {' ': '%20', '!': '%21', '"': '%22', '#': '%23', '$': '%24',
              '%': '%25', '&': '%26', "'": '%27', '(': '%28', ')': '%29',
              '*': '%2A', '+': '%2B', ',': '%2C', '-': '%2D', '.': '%2E',
              '/': '%2F', '0': '%30', '1': '%31', '2': '%32', '3': '%33',
              '4': '%34', '5': '%35', '6': '%36', '7': '%37', '8': '%38',
              '9': '%39', ':': '%3A', ';': '%3B', '<': '%3C', '=': '%3D',
              '>': '%3E', '?': '%3F', '@': '%40', 'A': '%41', 'B': '%42',
              'C': '%43', 'D': '%44', 'E': '%45', 'F': '%46', 'G': '%47',
              'H': '%48', 'I': '%49', 'J': '%4A', 'K': '%4B', 'L': '%4C',
              'M': '%4D', 'N': '%4E', 'O': '%4F', 'P': '%50', 'Q': '%51',
              'R': '%52', 'S': '%53', 'T': '%54', 'U': '%55', 'V': '%56',
              'W': '%57', 'X': '%58', 'Y': '%59', 'Z': '%5A', '[': '%5B',
              '\\': '%5C', ']': '%5D', '^': '%5E', '_': '%5F', '`': '%60',
              'a': '%61', 'b': '%62', 'c': '%63', 'd': '%64', 'e': '%65',
              'f': '%66', 'g': '%67', 'h': '%68', 'i': '%69', 'j': '%6A',
              'k': '%6B', 'l': '%6C', 'm': '%6D', 'n': '%6E', 'o': '%6F',
              'p': '%70', 'q': '%71', 'r': '%72', 's': '%73', 't': '%74',
              'u': '%75', 'v': '%76', 'w': '%77', 'x': '%78', 'y': '%79',
              'z': '%7A', '{': '%7B', '|': '%7C', '}': '%7D', '~': '%7E',
              ' ': '%7F', '`': '%80', '': '%81', '‚': '%82', 'ƒ': '%83',
              '„': '%84', '…': '%85', '†': '%86', '‡': '%87', 'ˆ': '%88',
              '‰': '%89', 'Š': '%8A', '‹': '%8B', 'Œ': '%8C', '': '%8D',
              'Ž': '%8E', '': '%8F', '': '%90', '‘': '%91', '’': '%92',
              '“': '%93', '”': '%94', '•': '%95', '–': '%96', '—': '%97',
              '"': '%98', '™': '%99', 'š': '%9A', '›': '%9B', 'œ': '%9C',
              '': '%9D', 'ž': '%9E', 'Ÿ': '%9F', ' ': '%A0', '¡': '%A1',
              '¢': '%A2', '£': '%A3', '¤': '%A4', '¥': '%A5', '¦': '%A6',
              '§': '%A7', '¨': '%A8', '©': '%A9', 'ª': '%AA', '«': '%AB',
              '¬': '%AC', "": '%AD', '®': '%AE', '¯': '%AF', '°': '%B0',
              '±': '%B1', '²': '%B2', '³': '%B3', '´': '%B4', 'µ': '%B5',
              '¶': '%B6', '·': '%B7', '¸': '%B8', '¹': '%B9', 'º': '%BA',
              '»': '%BB', '¼': '%BC', '½': '%BD', '¾': '%BE', '¿': '%BF',
              'À': '%C0', 'Á': '%C1', 'Â': '%C2', 'Ã': '%C3', 'Ä': '%C4',
              'Å': '%C5', 'Æ': '%C6', 'Ç': '%C7', 'È': '%C8', 'É': '%C9',
              'Ê': '%CA', 'Ë': '%CB', 'Ì': '%CC', 'Í': '%CD', 'Î': '%CE',
              'Ï': '%CF', 'Ð': '%D0', 'Ñ': '%D1', 'Ò': '%D2', 'Ó': '%D3',
              'Ô': '%D4', 'Õ': '%D5', 'Ö': '%D6', '×': '%D7', 'Ø': '%D8',
              'Ù': '%D9', 'Ú': '%DA', 'Û': '%DB', 'Ü': '%DC', 'Ý': '%DD',
              'Þ': '%DE', 'ß': '%DF', 'à': '%E0', 'á': '%E1', 'â': '%E2',
              'ã': '%E3', 'ä': '%E4', 'å': '%E5', 'æ': '%E6', 'ç': '%E7',
              'è': '%E8', 'é': '%E9', 'ê': '%EA', 'ë': '%EB', 'ì': '%EC',
              'í': '%ED', 'î': '%EE', 'ï': '%EF', 'ð': '%F0', 'ñ': '%F1',
              'ò': '%F2', 'ó': '%F3', 'ô': '%F4', 'õ': '%F5', 'ö': '%F6',
              '÷': '%F7', 'ø': '%F8', 'ù': '%F9', 'ú': '%FA', 'û': '%FB',
              'ü': '%FC', 'ý': '%FD', 'þ': '%FE', 'ÿ': '%FF'}

ROMAN_NUMERALS = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
ROMAN_DOUBLES = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}

romerals = (("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90),
            ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1))

GREEK_ALPHABET = {"α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta",
                  "ε": "epsilon", "ζ": "zeta", "η": "eta", "θ": "theta",
                  "ι": "iota", "κ": "kappa", "λ": "lambda", "μ": "mu",
                  "ν": "nu", "ξ": "xi", "ο": "omicron", "π": "pi",
                  "ρ": "rho", "σ": "sigma", "τ": "tau", "υ": "upsilon",
                  "φ": "phi", "χ": "chi", "ψ": "psi", "ω": "omega"}

backslash = '\\'
backspace = '\b'
newline = '\n'
tabulate = '\t'
singlequote = '\''
doublequote = '\"'
bell = '\a'
octal = '\o84'
hexe = '\xFF'
escape_characters = [backslash, backspace, newline, tabulate, singlequote, doublequote, bell, octal, hex]
recursion = '…'
octothrope = '#'

REPL = ["Read", "Eval", "Print", "Loop"]


def memoise(function):
    cache = {}

    def memoised(*args):
        if args not in cache:
            cache[args] = function(*args)
        return cache[args]

    return memoised


def input_int(prompt, low=0, high=0):
    """
    age = input_int('Enter your age (minimum: 13): ',13,120)
    """
    valid = False
    if not low == high:
        low, high = (min(low, high), max(low, high))
        limits = str("(Between {0:d} and {1:d}): ".format(low, high))
    else:
        limits = ""
    while not valid:
        try:
            whole = int(input(prompt + limits))
        except ValueError:
            continue
        except SyntaxError:
            continue
        else:
            if (whole >= low) and (whole <= high):
                valid = True
    return whole


def input_float(prompt, low=0, high=0):
    valid = False
    if not low == high:
        low, high = (min(low, high), max(low, high))
        limits = str("(Between {0:d} and {1:d}): ".format(low, high))
    else:
        limits = ""
    while not valid:
        try:
            real = float(input(prompt + limits))
        except ValueError:
            continue
        except SyntaxError:
            continue
        else:
            if (real >= low) and (real <= high):
                valid = True
    return real


def input_string(prompt, low= 0, high= 0):
    """
    password = input_string('Enter a password: ', 3, 8)
    continue = input_string('Press Enter to continue: ', 0, 0)
    """
    valid = False
    low, high = abs(low), abs(high)
    low, high = (min(low, high), max(low, high))
    if high > 0:
        if not low == high:
            limits = str("(Must be between {0:d} and {1:d} characters in length): "
                         .format(low, high))
        elif low == high:
            limits = str("(Must be between {0:d} characters in length): "
                         .format(high))
    else:
        limits = ""
    while not valid:
        try:
            string = input(str(prompt + limits))
        except ValueError:
            continue
        except SyntaxError:
            continue
        else:
            if not high == 0:
                valid = len(string) in range(low, high + 1)
            else:
                valid = True
    return string


def input_date(prompt, example, expect):
    """
    birthday = input_datetime('Enter date of birth ', 'YYYY/MM/DD', '%Y/%m/%d')
    """
    valid = False
    while not valid:
        enteredate = input(prompt + '(' + example + '): ')
        try:
            datentered = datetime.datetime.strptime(enteredate, expect)
            # print (enteredate, datentered)
        except ValueError:
            # print('ValueError')
            print('A valid date needs to be entered in the expected format')
            continue
        except SyntaxError:
            # print('SyntaxError')
            print('Date needs to be entered in expected format')
            continue
        else:
            valid = True
    return datentered.strftime(expect)


def input_time(prompt, example, expect):
    """
    eventime = input_time('Enter time of event ', 'HH:MM:ss', '%H:%M:%S')
    """
    valid = False
    while not valid:
        enteredtime = input(prompt + '(' + example + '): ')
        try:
            timentered = datetime.datetime.strptime(enteredtime, expect)
            # print (enteredtime, timentered)
        except ValueError:
            # print('ValueError')
            print('A valid time needs to be entered in the expected format')
            continue
        except SyntaxError:
            # print('SyntaxError')
            print('Time needs to be entered in expected format')
            continue
        else:
            valid = True
    return timentered.strftime(expect)


def input_choice(prompt, strings, fails=False):
    """
    selection = ['yes', 'y', 'no', 'n']
    confirm = input_choice("Enter 'Yes' or 'No' to continue: ", selection)
    
    selection = ['male', 'm', 'female', 'f']
    confirm = input_choice("Enter sex as 'Male' or 'Female': ", selection)
    """
    valid = False
    invalids = []
    strings = [str(option).strip().lower() for option in strings]
    while not valid:
        choice = input(prompt).strip().lower()
        try:
            choice in strings
        except ValueError:
            continue
        except SyntaxError:
            continue
        invalids.append(choice)
        valid = choice in strings

    if fails:
        return choice, invalids
    else:
        return choice


def romanise(number):
    """
    Convert number to roman numeral
    >>> romanise(2222)
    'MMCCXXII'
    >>> romanise(1443)
    'MCDXLIII'
    >>> romanise(3108)
    'MMMCVIII'
    """
    romber = []
    for romeral, integer in romerals:
        (tally, number) = divmod(number, integer)
        romber += [romeral * tally]
    return "".join(romber)


def numerise(romber):
    """
    Convert roman numeral to integer
    >>> numerise('MMCCXXII')
    2222
    >>> numerise('CMCDXCXLIXIV')
    1443
    >>> numerise('MCDXLIII')
    1443
    >>> numerise('MCMDCDCXCLXLXIXVIV')
    3108
    >>> numerise('MMMCVIII')
    3108
    """
    number = 0
    index = 0
    for romeral, integer in romerals:
        while romber[index: index + len(romeral)] == romeral:
            number += integer
            index += len(romeral)
    return number


def morse_code(string):
    return ' '.join(MORSE_CODE.get(char.upper(), char) for char in string)


def phonic_code(string):
    return ' '.join(PHONIC_CODE.get(char.upper(), char) for char in string)


def letter_sounds(string):
    return ' '.join(SPELL_LETTERS.get(char.upper(), char) for char in string)


def str2bits(string):
    def convert_str2bits(text_string):
        for char in text_string:
            number = ord(char)
            for bit in '{0:0=#10b}'.format(number)[2:]:
                yield int(bit)

    return list(convert_str2bits(string))


def grouper(n, iterable, fillvalue=None):
    # Source: http://docs.python.org/library/itertools.html#recipes
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    return itertools.zip_longest(*[iter(iterable)] * n, fillvalue=fillvalue)


def bits2str(bits):
    def convert_bits2str(bits_list):
        for bit in grouper(8, bits_list):
            yield chr(int(''.join(map(str, bit)), 2))

    return ''.join(convert_bits2str(bits))


# list(bin(my_num)[2:].zfill(8))

def binstr2dec(string):
    """
    Convert a string of binary bits to a decimal number
    >>> binstr2dec("100100101001")
    2345
    """
    return int(string, 2)


def dec2binstr(number):
    return bin(number)[2:]


def dec2hexstr(number):
    return hex(number)[2:]


bin2dec = lambda s: sum(int(j) * pow(2, i) for i, j in enumerate(reversed(s)))


def bin2string(binstring):
    """
    >>> print (bin2string("01100110 01100101 01100101 01101100 01101001 01101110 01100111 00100000 01101100 01110101 01100011 01101011 01111001 00001010"))
    feeling lucky
    <BLANKLINE>
    """
    # return (''.join(chr(bin2dec(bit)) for bit in binstring.split()))
    return "".join(chr(int(bit, 2)) for bit in binstring.split())


"""
add = lambda x,y : x + y
reduce(add, [int(x) * 2 ** y for x, y in zip(list(binstr), range(len(binstr) - 1, -1, -1))])
"""

"""
Rules
"|0" -> "0||"
"1" -> "0|"
"0" -> ""

Symbol string
"101"

Execution
"0|01"
"00||1"
"00||0|"
"00|0|||"
"000|||||"
"00|||||"
"0|||||"
"|||||"

"""


def count_vowels(string):
    """ (str) -> int

    >>> count_vowels("string")
    1
    """

    def test_count_vowels(self):
        string = "string"
        actual = count_vowels(string)
        expected = 1
        self.assertEqual(actual, expected)

    vowels = GLOBAL_EN_VOWELS
    num_vowels = 0
    for character in string:
        if character in vowels:
            num_vowels += 1
    return num_vowels


def extract_vowels(string):
    """ (str) -> str

    >>> extract_vowels("string")
    'i'
    """

    def test_extract_vowels(self):
        test_string = "string"
        actual = extract_vowels(test_string)
        expected = 'i'
        self.assertEqual(actual, expected)

    vowels = GLOBAL_EN_VOWELS
    num_vowels = 0
    collector = []
    for character in string:
        if character in vowels:
            collector.append(character)
    return "".join(collector)


def extract_digits(string):
    """ (str) -> str

    >>> extract_digits("5tr1ng")
    '51'
    """

    def test_extract_digits(self):
        test_string = "5tr1ng"
        actual = extract_digits(test_string)
        expected = '51'
        self.assertEqual(actual, expected)

    digits = []
    for character in string:
        if character.isdigit():
            digits.append(character)
    return "".join(digits)


def extract_numbers(string):
    """
    >>> extract_numbers(".1 .12 9.1 98.1 1. 12. 1 12 -1 +1 2e9 +2E+09 -2e-9 -3")
    ['.1', '.12', '9.1', '98.1', '1', '12', '1', '12', '-1', '+1', '2', '9', '+2', '+09', '-2', '-9', '-3']
    """
    return re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", string)


def extract_only_digits(string):
    return ''.join(char for char in string if char.isdigit())
    # return filter(lambda char: char.isdigit(), string)
    # return re.sub(REGEX_DIGITS, "", string)


def extract_only_letters(string):
    return ''.join(char for char in string if char.isalpha())
    # return filter(lambda char: char.isalpha(), string)
    # return re.sub(REGEX_LETTERS, "", string)


def regex_filter(string, regex):
    return re.sub(regex, "", string)


def capitalise(string):
    return ' '.join(char.capitalize() for char in string.split(' '))


def containsAny(string, strings):
    """Check whether 'str' contains ANY of the chars in 'strings'"""
    return 1 in [c in string for c in strings]


def containsAll(string, strings):
    """Check whether 'str' contains ALL of the chars in 'strings'"""
    return 0 not in [c in string for c in strings]


def contains_any(string, strings):
    """Check whether 'str' contains ANY of the chars in 'strings'"""
    for c in strings:
        if c in string:
            return 1
    return 0


def contains_all(string, strings):
    """Check whether 'str' contains ALL of the chars in 'strings'"""
    for c in strings:
        if c not in string:
            return 0
    return 1


def add_to_letter_counts(dictonary, string):
    '''(dict of {str: int}, str) -> NoneType

    d is a dictionary where the keys are single-letter strings and the values
    are counts.

    For each letter in s, add to that letter's count in d.

    Precondition: all the letters in s are keys in d.
    '''

    for character in string:
        dictonary[character] += 1
    return None


def common_characters(first, second):
    '''(str, str) -> str

    Return a new string containing all characters from s1 that appear at least
    once in s2.  The characters in the result will appear in the same order as
    they appear in s1.

    >>> common_characters('abc', 'ad')
    'a'
    >>> common_characters('a', 'a')
    'a'
    >>> common_characters('abb', 'ab')
    'abb'
    >>> common_characters('abracadabra', 'ra')
    'araaara'
    '''

    result = []

    for character in first:
        if character in second:
            result.append(character)  # BODY MISSING

    return "".join(result)


def reverse_string_iter(string):
    """ (str) -> str

    >>> reverse_string_iter('string of text')
    'txet fo gnirts'
    """

    reverse = []

    ##    remaining = 0
    ##    while remaining < len(string):
    ##        reverse = string[remaining] + reverse
    ##        remaining += 1

    remaining = len(string) - 1
    while remaining >= 0:
        reverse.append(string[remaining])
        remaining -= 1

    return "".join(reverse)


def reverse_string_loop(string):
    """ (str) -> str

    >>> reverse_string_loop('string of text')
    'txet fo gnirts'
    """

    reverse = ""
    for character in string:
        reverse = character + reverse
    return reverse


@memoise
def reverse_string_recurse(string):
    """ (str) -> str

    >>> reverse_string_recurse('string of text')
    'txet fo gnirts'
    """

    if string == '':
        return string
    return reverse_string(string[1:]) + string[0]


def reverse_string_list(string):
    string = list(string)
    string.reverse()
    return "".join(string)


def reverse_string(string):
    return string[::-1]


def reverse_words(string):
    # return ' '.join(reversed(string.split(' ')))
    return ' '.join(string.split(' ')[::-1])


def find_replace(string, search, replace=""):
    return string.replace(search, replace)


def flip_text(string):
    reverse = reversed(string)
    flipped = ""
    for character in reverse:
        if character in FLIP_TABLE:
            flipped += FLIP_TABLE[character]
        else:
            flipped += character
    return flipped


def palindrome_reverse(string):
    """ (str) -> bool

    Return True if and only if string is a palindrome
    
    >>> palindrome_reverse('level')
    True
    >>> palindrome_reverse('even')
    False
    """

    # Compare the string to the reverse of the string
    return string == reverse_string(string)


def palindrome_split(string):
    """ (str) -> bool

    Return True if and only if string is a palindrome
    
    >>> palindrome_split('level')
    True
    >>> palindrome_split('even')
    False
    """

    length = len(string)
    half = length // 2

    # Compare the first half of the string to the second half using indices
    # Middle character of odd length strings is omitted using decimal division
    return string[:half] == reverse_string(string[length - half:])


def palindrome_compare(string):
    """ (str) -> bool

    Return True if and only if string is a palindrome
    
    >>> palindrome_compare('level')
    True
    >>> palindrome_compare('even')
    False
    """

    left = 0
    right = len(string) - 1

    while left < right and string[left] == string[right]:
        left += 1
        right -= 1
    # If string is empty, right is less than left, so loop terminates
    # If string is a single character, left and right are equal
    return right <= left


def palindrome_loop(string):
    """ (str) -> bool

    Return True if and only if string is a palindrome
    
    >>> palindrome_loop('level')
    True
    >>> palindrome_loop('even')
    False
    """

    right = len(string) - 1
    for left in range(len(string) // 2):
        if string[left] != string[right - left]:
            return False
    return True


def count_words(content):
    """
    str or list -> dict {"str" : int}
    
    Returns a dictionary of words and their counts from a list or string
    """
    if type(content) == str:
        if content == "":
            return None
        content = content.split()
    if type(content) == list:
        if not content:
            return None
        content = [extract_only_letters(word) for word in content]

    word_counts = {}
    for word in content:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
    return word_counts


def map_words(content):
    return sorted([(word, 1) for word in content])


def reduce_words(content):
    word_totals = {}
    for word in content:
        if word[0] in word_totals:
            word_totals[word[0]] += 1
        else:
            word_totals[word[0]] = 1
    return word_totals


def mapreduce_count_words(content):
    """
    str or list -> dict {"str" : int}
    
    Returns a dictionary of words and their counts from a list or string
    """
    if type(content) == str:
        if content == "":
            return None
        content = content.split()
    if type(content) == list:
        if not content:
            return None
        content = [regex_filter(word, REGEX_LETTERS) for word in content]

    words_mapped = map_words(content)
    words_reduced = reduce_words(words_mapped)
    return sum(words_reduced.values())


def mapreduce_word_counts(content):
    """
    str or list -> dict {"str" : int}
    
    Returns a dictionary of words and their counts from a list or string
    """
    if type(content) == str:
        if content == "":
            return None
        content = content.split()
    if type(content) == list:
        if not content:
            return None
        content = [regex_filter(word, REGEX_LETTERS) for word in content]

    words_mapped = map_words(content)
    words_reduced = reduce_words(words_mapped)
    return sorted(words_reduced.items())


def mapreduce_unique_words(content):
    """
    str or list -> dict {"str" : int}
    
    Returns a dictionary of words and their counts from a list or string
    """
    if type(content) == str:
        if content == "":
            return None
        content = content.split()
    if type(content) == list:
        if not content:
            return None
        content = [regex_filter(word, REGEX_LETTERS) for word in content]

    words_mapped = map_words(content)
    words_reduced = reduce_words(words_mapped)
    return sorted(words_reduced.keys()), len(words_reduced)


def mapreduce_solo_words(content):
    """
    str or list -> dict {"str" : int}
    
    Returns a dictionary of words and their counts from a list or string
    """
    if type(content) == str:
        if content == "":
            return None
        content = content.split()
    if type(content) == list:
        if not content:
            return None
        content = [regex_filter(word, REGEX_LETTERS) for word in content]

    words_mapped = map_words(content)
    words_reduced = reduce_words(words_mapped)
    return sorted(word for word, count in words_reduced.items()
                  if count == 1)


def total_words(word_counts):
    """
    dict {"str" : int} -> int
    
    Returns the total sum of words from a dictionary of words and their counts
    """

    if type(word_counts) != dict:
        if type(word_counts) == str or type(word_counts) == list:
            word_counts = count_words(word_counts)
            # return None

    word_counter = 0
    for word in word_counts:
        word_counter += word_counts[word]
    return word_counter


def common_word(word_counts):
    """
    dict {"str" : int} -> tuple("str", int)
    
    Returns the most common word and its count from a dictionary of words
    and their counts.
    """

    if type(word_counts) != dict:
        if type(word_counts) == str or type(word_counts) == list:
            word_counts = count_words(word_counts)
            # return None

    most_used = ""
    word_count = 0
    for word, count in word_counts.items():
        if count > word_count:
            most_used = word
            word_count = count
    return most_used, word_count


def unique_words(word_counts):
    """
    dict {"str" : int} -> list["str"]

    Returns a list of words with count of one from a dictionary of words
    and their counts.
    """

    if type(word_counts) != dict:
        if type(word_counts) == str or type(word_counts) == list:
            word_counts = count_words(word_counts)
            # return None

    used_once = []
    for word, count in word_counts.items():
        if count == 1:
            used_once.append(word)
    return used_once


def swap_words(two_words):
    """(str) -> str

    Precondition: two_words is a string containing two words separated by one space.

    Return a new string where the words are in reverse order, again separated by
    one space.

    >>> swap_words('Hello World')
    'World Hello'
    """

    first = two_words[:two_words.find(' ')]
    second = two_words[two_words.find(' ') + 1:]
    return second + ' ' + first


def is_anagram(first, second):
    """ (str, str) -> bool

    Return True if first is an anagram of second.

    >>> is_anagram("silent", "listen")
    True
    >>> is_anagram("admirer", "married")
    True
    >>> is_anagram("bear", "breach")
    False
    """

    # If the words aren't the same length, there is no need to compare them
    if len(first) != len(second):
        return False

    words = [[], []]
    # Build lists from the characters in the words
    for character in range(len(first)):
        words[0].append(first[character])
        words[1].append(second[character])
    words[0].sort()
    words[1].sort()
    return words[0] == words[1]


def count_startswith_reduce(word_list, character):
    """ (list of str, str) -> int

    Precondition: the length of each item in L is >= 1, and len(ch) == 1

    Return the number of strings in L that begin with ch.

    >>> count_startswith_reduce(['rumba', 'salsa', 'samba'], 's')
    2
    """

    startswith = word_list[:]
    for word in word_list:
        if word.startswith(character):
            startswith.remove(word)

    return len(word_list) - len(startswith)


def count_startswith_build(word_list, character):
    """ (list of str, str) -> int

    Precondition: the length of each item in L is >= 1, and len(ch) == 1

    Return the number of strings in L that begin with ch.

    >>> count_startswith_build(['rumba', 'salsa', 'samba'], 's')
    2
    """

    startswith = []
    for word in word_list:
        if word.startswith(character):
            startswith.append(word)

    return len(startswith)


def both_start_with(first, second, prefix):
    """(str, str, str) -> bool

    Return True if and only if first and second both start with the letters in prefix.
    """
    return upper(first.startswith(prefix)) and upper(second.startswith(prefix))


def unique_values(dictionary):
    """ (dict) -> bool

    Return True if no two keys of dictionary map to the same value.

    >>> unique_values ({'a': 1, 'b': 2, 'c': 3})
    True
    >>> unique_values ({'a': 1, 'b': 2, 'c': 1})
    False
    >>> unique_values ({})
    True
    """

    seen = []  # The values that have been seen so far.
    for key in dictionary:
        if dictionary[key] in seen:
            return False
        else:
            seen.append(dictionary[key])

    return True


def return_list(string, delimiter):
    list_from_string = []
    sub_string = ''
    for character in string:
        if character != delimiter:
            sub_string += character
        else:
            list_from_string.append(sub_string)
            sub_string = ''
    list_from_string.append(sub_string)
    return list_from_string


def get_MAC_address():
    return ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0, 8 * 6, 8)][::-1])


def get_MAC_regex():
    return ':'.join(re.findall('..', '%012x' % uuid.getnode()))


def little_endian(string):
    return struct.unpack('<L', b"/%1".string)


if __name__ == '__main__':
    doctest.testmod()
    unittest.main(exit=False)
    print(get_MAC_address())
    print(get_MAC_regex())

"""
pat = re.compile('[\w-]*$')
pat_inv = re.compile ('[^\w-]')
allowed_chars=string.ascii_letters + string.digits + '_-'
allowed_set = set(allowed_chars)
trans_table = string.maketrans('','')

def check_set_diff(s):
    return not set(s) - allowed_set

def check_set_all(s):
    return all(x in allowed_set for x in s)

def check_set_subset(s):
    return set(s).issubset(allowed_set)

def check_re_match(s):
    return pat.match(s)

def check_re_inverse(s): # Search for non-matching character.
    return not pat_inv.search(s)

def check_trans(s):
    return not s.translate(trans_table,allowed_chars)

test_long_almost_valid='a_very_long_string_that_is_mostly_valid_except_for_last_char'*99 + '!'
test_long_valid='a_very_long_string_that_is_completely_valid_' * 99
test_short_valid='short_valid_string'
test_short_invalid='/$%$%&'
test_long_invalid='/$%$%&' * 99
test_empty=''

def main():
    funcs = sorted(f for f in globals() if f.startswith('check_'))
    tests = sorted(f for f in globals() if f.startswith('test_'))
    for test in tests:
        print ("Test %-15s (length = %d):" % (test, len(globals()[test])))
        for func in funcs:
            print ("  %-20s : %.3f" %
                   (func, timeit.Timer('%s(%s)' % (func, test),
                                 'from __main__ import pat,allowed_set,%s' %
                                 ','.join(funcs+tests)).timeit(10000)))
        print
                 

if __name__=='__main__': main()
"""
