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

import datetime
import hashlib
import itertools
import doctest
import keyword
import random
import re
import unittest

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

from vectors import Vector

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

ZODIAC_HOUSES = {'Aries': '♈', 'Tauras': '♉', 'Gemini': '♊',
                 'Cancer': '♋', 'Leo': '♌', 'Virgo': '♍', 'Libra': '♎',
                 'Scorpio': '♏', 'Ophiuchus': '⛎', 'Sagittarius': '♐',
                 'Capricorn': '♑', 'Aquarius': '♒', 'Pisces': '♓'}

CONSTELLATIONS = {'Aries': (18, 13), 'Tauras': (13, 21), 'Gemini': (21, 20),
                  'Cancer': (20, 10), 'Leo': (10, 16), 'Virgo': (16, 30),
                  'Libra': (30, 23), 'Scorpio': (23, 29), 'Ophiuchus': (29, 17),
                  'Sagittarius': (17, 20), 'Capricorn': (20, 16), 'Aquarius': (16, 11),
                  'Pisces': (11, 18)}

ZODIAC_DATES = {'Aries': (21, 20), 'Tauras': (21, 21), 'Gemini': (22, 21),
                'Cancer': (22, 22), 'Leo': (23, 22), 'Virgo': (23, 22),
                'Libra': (23, 22), 'Scorpio': (23, 22), 'Sagittarius': (23, 21),
                'Capricorn': (22, 20), 'Aquarius': (21, 19), 'Pisces': (20, 20)}

DAYS_IN_MONTH = {'January': 31, 'February': 28, 'March': 31, 'April': 30,
                 'May': 31, 'June': 30, 'July': 31, 'August': 31,
                 'September': 30, 'October': 31, 'November': 30, 'December': 31}

ZODIAC_SEASONS = {'Spring': ['Aries', 'Tauras', 'Gemini'],
                  'Summer': ['Cancer', 'Leo', 'Virgo'],
                  'Autumn': ['Libra', 'Scorpio', 'Ophiuchus', 'Sagittarius'],
                  'Winter': ['Caprocorn', 'Aquarius', 'Pisces']}

KEMET_SEASONS = {'Akhet': ["Djehuty", "Pa-en-Opet", "Hethert", "Ka-her-ka"],
                 'Peret': ["Ta'abet", "Pa-en-mekher", "Pa-en-Amenhotep", "Pa-en-Renenutet"],
                 'Shomu': ["Pa-en-Khonsu", "Pa-en-inet", "Ipip", "Mesut-Ra-Heruakhety"]}

STORMS = {'Hurricane': ['North Atlantic', 'South Atlantic', 'Northeast Pacific'],
          'Typhoon': ['Northwest Pacific'],
          'Cyclone': ['South Pacific', 'Indian Ocean']}

MOTIONS = ['Translational', 'Rotational', 'Periodic']

GRIEF_STAGES = ['Denial', 'Anger', 'Bargaining', 'Depression', 'Acceptance']

EQUINOX = ['Spring', 'Autumn']
SOLSTICE = ['Summer', 'Winter']

DAYS_IN_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# STARS = ['Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn', 'Sun']

DRAUGHTS_BW = {'Man': ('\u26C2', '\u26C0'), 'King': ('\u26C3', '\u26C1')}

CHESS_BW = {'King': ('\u265A', '\u2654'), 'Queen': ('\u265B', '\u2655'),
            'Rook': ('\u265C', '\u2656'), 'Bishop': ('\u265D', '\u2657'),
            'Knight': ('\u265E', '\u2658'), 'Pawn': ('\u265F', '\u2659')}

QUEENS = ((0, 0, 0, 1, 0, 0, 0, 0),
          (0, 0, 0, 0, 0, 0, 1, 0),
          (0, 0, 1, 0, 0, 0, 0, 0),
          (0, 0, 0, 0, 0, 0, 0, 1),
          (0, 1, 0, 0, 0, 0, 0, 0),
          (0, 0, 0, 0, 1, 0, 0, 0),
          (1, 0, 0, 0, 0, 0, 0, 0),
          (0, 0, 0, 0, 0, 1, 0, 0))

SUITS = {'Diamonds': ['\u2662', '\u2666'],
         'Clubs': ['\u2663', '\u2667'],
         'Hearts': ['\u2661', '\u2665'],
         'Spades': ['\u2660', '\u2664']}

RANKS = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
         'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
         'Jack': 10, 'Queen': 10, 'King': 10}

CARDS = {**SUITS, **RANKS}

Black = (0, 0, 0)
Brown = (128, 0, 0)
Green = (0, 128, 0)
Navy = (0, 0, 128)
Red = (255, 0, 0)
Lime = (0, 255, 0)
Blue = (0, 0, 255)
Olive = (128, 128, 0)
Purple = (128, 0, 128)
Teal = (0, 128, 128)
Grey = (128, 128, 128)
Yellow = (255, 255, 0)
Fuchsia = (255, 0, 255)
Aqua = (0, 255, 255)
Silver = (192, 192, 192)
White = (255, 255, 255)

web_colours = {"Aqua": Aqua,
               "Black": Black,
               "Blue": Blue,
               "Brown": Brown,
               "Fuchsia": Fuchsia,
               "Green": Green,
               "Grey": Grey,
               "Lime": Lime,
               "Navy": Navy,
               "Olive": Olive,
               "Purple": Purple,
               "Red": Red,
               "Silver": Silver,
               "Teal": Teal,
               "White": White,
               "Yellow": Yellow}

text_fore = {"Black": 30,
             "Red": 31,
             "Green": 32,
             "Yellow": 33,
             "Blue": 34,
             "Purple": 35,
             "Cyan": 36,
             "White": 37}

text_back = {"Black": 40,
             "Red": 41,
             "Green": 42,
             "Yellow": 43,
             "Blue": 44,
             "Purple": 45,
             "Cyan": 46,
             "White": 47}

text_style = {"Normal": 0,
              "Bright": 1,
              "Underline": 2,
              "Negative1": 3,
              "Negative2": 5}


def colour_print(string, fore="Black", back="White", style="Normal"):
    if type(fore) == str:
        fore = text_fore[fore]
    if type(back) == str:
        back = text_back[back]
    if type(style) == str:
        style = text_style[style]
    output = "\033[" + str(style) + ";" + str(fore) + ";" + str(back) + "m "
    print(output + string)


##def print_format_table():
##    """
##    prints table of formatted text format options
##    """
##    for style in range(8):
##        for fg in range(30,38):
##            s1 = ''
##            for bg in range(40,48):
##                format = ';'.join([str(style), str(fg), str(bg)])
##                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
##            print(s1)
##        print('\n')
##
##print_format_table()

##from colorama import Fore, Style
##import sys
##
##class Highlight:
##  def __init__(self, clazz, color):
##    self.color = color
##    self.clazz = clazz
##  def __enter__(self):
##    print(self.color, end="")
##  def __exit__(self, type, value, traceback):
##    if self.clazz == Fore:
##      print(Fore.RESET, end="")
##    else:
##      assert self.clazz == Style
##      print(Style.RESET_ALL, end="")
##    sys.stdout.flush()
##
##with Highlight(Fore, Fore.GREEN):
##  print("this is highlighted")
##print("this is not")



RGB_light = ("Red", "Green", "Blue", "White")
CMY_kemet = ("Cyan", "Magenta", "Yellow", "Black")
RYB_paint = ("Red", "Yellow", "Blue", Grey)
colours = RGB_light + CMY_kemet

Colour_HEX_codes = {"Black": "000000",
                    "Red": "FF0000",
                    "Orange": "FF7F00",
                    "Yellow": "FFFF00",
                    "Chartreuse": "7FFF00",
                    "Green": "00FF00",
                    "Spring Green": "00FF7F",
                    "Grey": "7F7F7F",
                    "Cyan": "00FFFF",
                    "Azure": "007FFF",
                    "Blue": "0000FF",
                    "Purple": "7F00FF",
                    "Magenta": "FF00FF",
                    "Rose": "FF007F",
                    "White": "FFFFFF"}

DNA = {'A': Blue, 'T': Yellow, 'G': Green, 'C': Red, 'X': Aqua, 'Y': Fuchsia, 'Z': Teal}

DNA_BASES = {'Adenine': Blue, 'Thymine': Yellow, 'Guanine': Green,
             'Cytosine': Red, 'dNaM': Aqua, 'dTPT3': Fuchsia, 'd5SICS': Teal}

Remember_planet_order = "My Very Easy Method Just Simplifies Us Naming Planets"
# Planet: [orbit speed km/sec, orbit speed mph, gravity m/s^2,
#          distance of orbit in miles 10^6, miles diameter]
# http://nssdc.gsfc.nasa.gov/planetary/factsheet/
PLANETS = {'Mercury': (47.8725, 107082, 3.703, 233.7, 1516),
           'Venus': (35.0214, 78350, 8.872, 422.5, 3761),
           'Earth': (29.7859, 66630, 9.8067, 584, 3959),
           'Mars': (24.1309, 54000, 3.728, 888, 2460),
           'Jupiter': (13.0697, 29240, 25.93, 3037, 43441),
           'Saturn': (9.6724, 21640, 11.9, 5565.9, 36184),
           'Uranus': (6.8352, 15290, 9.01, 11201.3, 15759),
           'Neptune': (5.4778, 12250, 11.28, 17562.3, 15299),
           'Pluto': (4.783328, 10700, 0.610, 22695.7, 1186)}

DATA_SCIENCE_QUESTIONS = ["Descriptive", "Exploratory", "Inferential",
                          "Predictive", "Casual", "Mechanistic"]

CONTINENTS_AREA = {"Asia": (17139445, 4055000000),
                   "Africa": (11677239, 1108500000),
                   "North America": (9361791, 522807432),
                   "South America": (6880706, 379919602),
                   "Antarctica": (5500000, 4000),
                   "Europe": (3997929, 729871042),
                   "Australia": (2967909, 20434176)}


def any_colour():
    return web_colours[random.randrange(0, len(web_colours))]


DICEFACE = {1: '\u2680', 2: '\u2681', 3: '\u2682',
            4: '\u2683', 5: '\u2684', 6: '\u2685'}


def roll_dice(sides=6):
    # return random.randrange(1, sides + )
    return random.randint(1, sides)


def multi_roll(rolls=6, sides=6):
    """
    Returns a list containing a given number of dice rolls
    """
    return [roll_dice(sides) for roll in range(rolls)]


def face_values(rolls):
    """
    Returns a dictionary histogram of dice roll frequencies from a list of dice rolls
    face_values(multi_roll(46656) )
    """
    values = {}
    for roll in rolls:
        values[roll] = values.get(roll, 0) + 1
    return values


def face_product(rolls):
    result = 1
    for roll in rolls:
        result *= roll
    return result


def rate_faces(values):
    """
    Returns a dictionary with the normalised probability mass function
    from a dictionary of dice roll frequencies
    rate_faces(face_values(multi_roll(46656) ) )
    """
    ratings = float(len(values))
    pmf = {}
    for face, frequency in values.items():
        pmf[face] = frequency / ratings
    return pmf


def best_face(values):
    """
    Returns the most frequent face value from a dictionary
    of dice roll fequencies
    best_face(face_values(multi_roll(46656) ) )
    """
    best = None
    score = 0
    for face, frequency in values.items():
        if frequency > score:
            best = face
            score = frequency
    return best


def roll_event(event):
    """
    Returns a boolean based on whether a dice roll is from the list of matches
    roll_event([2, 4, 6])
    """
    return roll_dice() in event


def roll_sample(trials, event):
    """
    Returns a list of booleans based on whether multiple dice rolls are from
    the list of matches
    roll_sample(trials, event = [1, 3, 5])
    """
    return [roll_event(event) for trial in range(trials)]


def dice_rolls(rolls=6):
    """
    Returns the unicode characters representing dice face values
    """
    return [DICEFACE[roll_dice(6)] for roll in range(rolls)]


COINSIDE = {1: 'Heads', 2: 'Tails'}


def flip_coin():
    return random.randint(1, 2)


def coin_flips(flips=3):
    """
    Returns a list of results from flipping a coin. (Default coin flips is 3)
    """
    return [COINSIDE[flip_coin()] for flip in range(flips)]


def flip_best_of(maximum):
    lead = 0
    reach = maximum // 2 + 1
    track = {}
    if maximum == 0:
        return track
    while lead != reach:
        flip = flip_coin()
        track[COINSIDE[flip]] = track.get(COINSIDE[flip], 0) + 1
        if track[COINSIDE[flip]] > lead:
            lead = track[COINSIDE[flip]]
    return track


def fizzbuzz(integer):
    string = str(integer)
    if integer % 15 == 0:
        string = "FizzBuzz"
    elif integer % 5 == 0:
        string = "Buzz"
    elif integer % 3 == 0:
        string = "Fizz"
    return string
print ([fizzbuzz(question) for question in range(-15,16)])


def fizzbuzzrange(start, stop):
    return [fizzbuzz(integer) for integer in range(start, stop)]


def fizzbuzzlist(start, stop):
    return ["Fizz" * (not integer % 3) +
            "Buzz" * (not integer % 5) or
            str(integer) for integer in range(start, stop)]


def day_of_week(year, month, day, origin=0):
    """
    Tomohiko Sakamoto's 
    >>> day_of_week(1582,10,4,9)
    'Thursday'
    >>> day_of_week(1582,10,15,-1)
    'Friday'
    >>> day_of_week(1752,9,2,11)
    'Wednesday'
    >>> day_of_week(1752,9,14)
    'Thursday'
    """
    days2shift = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    day = day % 7
    month = month % 12
    year -= month < 3
    return DAYS_IN_WEEK[int(year + (year / 4) - (year / 100) + (year / 400) +
                            days2shift[month - 1] + day + origin) % 7]


# int dow(int y, int m, int d){
#  static int t[] = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4}; 
#  y -= m < 3;
#  return (y + y/4 - y/100 + y/400 + t[m-1] + d + c) % 7;
# }

def current_day():
    currentDate = datetime.datetime.today().date()
    return day_of_week(currentDate.year, currentDate.month, currentDate.day)


def full_datetime_now(holocene = False):
    """http://strftime.org/"""
    currentDate = datetime.datetime.today().date()
    holoceneYear = int(currentDate.strftime('%Y')) + 10000
    
    print("Today is day {0:s} in week {1:s}, which is"
          .format(currentDate.strftime('%j'), currentDate.strftime('%U')))
    print(f"Today is day {currentDate.strftime('%j')} in week {currentDate.strftime('%U')}, which is")

    print(current_day(), currentDate.strftime('the %d of %B in the year %Y'))
    print(f"{current_day()} {currentDate.strftime('the %d of %B in the year %Y')}")
    
    if holocene:
        print("or the year", holoceneYear, "of the human era using the holocene calendar")
        print(f"or the year {holoceneYear} of the human era using the holocene calendar")

    currentTime = datetime.datetime.now().time()
    print(currentTime.strftime("and the time before you read this a moment ago was %H:%M:%S.%f"))
    print(f'{currentTime.strftime("and the time before you read this a moment ago was %H:%M:%S.%f")}')


def time_to_minutes(time_str):
    try:
        hours, minutes, seconds = time_str.split(':')
    except ValueError:
        return -1
    return int(hours) * 60 + int(minutes) + int(seconds) / 60.0


def time_to_seconds(time_str):
    try:
        hours, minutes, seconds = time_str.split(':')
    except ValueError:
        return -1
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)


# outcomes = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
outcomes = {"Red", "Green", "Blue"}


# outcomes = set(["Sunday", "Mondy", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

def gen_all_sequences(outcomes, length = 3):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """

    answer = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in answer:
            for item in outcomes:
                new_seq = list(seq)
                new_seq += [item]
                temp.add(tuple(new_seq))
        answer = temp
    return answer


def gen_permutations(elements):
    """
    Compute all permuations of elements.
    """
    stack = list(elements)
    results = [[stack.pop()]]
    while len(stack) != 0:
        item = stack.pop()
        new_results = []
        for perm in results:
            for i in range(len(perm) + 1):
                new_results.append(perm[:i] + [item] + perm[i:])
        results = new_results
    return results


def gen_sorted_sequences(outcomes, length=3):
    """
    Function that creates all sorted sequences via gen_all_sequences
    """
    all_sequences = gen_all_sequences(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)


# print (gen_all_sequences(outcomes, 3), '\n' )
# print (gen_permutations(outcomes), '\n' )
# print (gen_sorted_sequences(outcomes, 3), '\n' )



currency = {"AFN": "Afghanistan Afghani",
            "ALL": "Albania Lek",
            "DZD": "Algeria Dinar",
            "AOA": "Angola Kwanza",
            "ARS": "Argentina Peso",
            "AMD": "Armenia Dram",
            "AWG": "Aruba Guilder",
            "AUD": "Australia Dollar",
            "AZN": "Azerbaijan New Manat",
            "BSD": "Bahamas Dollar",
            "BHD": "Bahrain Dinar",
            "BDT": "Bangladesh Taka",
            "BBD": "Barbados Dollar",
            "BYR": "Belarus Ruble",
            "BZD": "Belize Dollar",
            "BMD": "Bermuda Dollar",
            "BTN": "Bhutan Ngultrum",
            "BOB": "Bolivia Boliviano",
            "BAM": "Bosnia and Herzegovina Convertible Marka",
            "BWP": "Botswana Pula",
            "BRL": "Brazil Real",
            "BND": "Brunei Darussalam Dollar",
            "BGN": "Bulgaria Lev",
            "BIF": "Burundi Franc",
            "KHR": "Cambodia Riel",
            "CAD": "Canada Dollar",
            "CVE": "Cape Verde Escudo",
            "KYD": "Cayman Islands Dollar",
            "CLP": "Chile Peso",
            "CNY": "China Yuan Renminbi",
            "COP": "Colombia Peso",
            "XOF": "Communauté Financière Africaine (BCEAO) Franc",
            "XAF": "Communauté Financière Africaine (BEAC) CFA Franc BEAC",
            "KMF": "Comoros Franc",
            "XPF": "Comptoirs Français du Pacifique (CFP) Franc",
            "CDF": "Congo/Kinshasa Franc",
            "CRC": "Costa Rica Colon",
            "HRK": "Croatia Kuna",
            "CUC": "Cuba Convertible Peso",
            "CUP": "Cuba Peso",
            "CZK": "Czech Republic Koruna",
            "DKK": "Denmark Krone",
            "DJF": "Djibouti Franc",
            "DOP": "Dominican Republic Peso",
            "XCD": "East Caribbean Dollar",
            "EGP": "Egypt Pound",
            "SVC": "El Salvador Colon",
            "ERN": "Eritrea Nakfa",
            "EEK": "Estonia Kroon",
            "ETB": "Ethiopia Birr",
            "EUR": "Euro Member Countries",
            "FKP": "Falkland Islands (Malvinas) Pound",
            "FJD": "Fiji Dollar",
            "GMD": "Gambia Dalasi",
            "GEL": "Georgia Lari",
            "GHS": "Ghana Cedi",
            "GHC": "Ghana Cedis",
            "GIP": "Gibraltar Pound",
            "GTQ": "Guatemala Quetzal",
            "GGP": "Guernsey Pound",
            "GNF": "Guinea Franc",
            "GYD": "Guyana Dollar",
            "HTG": "Haiti Gourde",
            "HNL": "Honduras Lempira",
            "HKD": "Hong Kong Dollar",
            "HUF": "Hungary Forint",
            "ISK": "Iceland Krona",
            "INR": "India Rupee",
            "IDR": "Indonesia Rupiah",
            "XDR": "International Monetary Fund (IMF) Special Drawing Rights",
            "IRR": "Iran Rial",
            "IQD": "Iraq Dinar",
            "IMP": "Isle of Man Pound",
            "ILS": "Israel Shekel",
            "JMD": "Jamaica Dollar",
            "JPY": "Japan Yen",
            "JEP": "Jersey Pound",
            "JOD": "Jordan Dinar",
            "KZT": "Kazakhstan Tenge",
            "KES": "Kenya Shilling",
            "KPW": "Korea (North) Won",
            "KRW": "Korea (South) Won",
            "KWD": "Kuwait Dinar",
            "KGS": "Kyrgyzstan Som",
            "LAK": "Laos Kip",
            "LVL": "Latvia Lat",
            "LBP": "Lebanon Pound",
            "LSL": "Lesotho Loti",
            "LRD": "Liberia Dollar",
            "LYD": "Libya Dinar",
            "LTL": "Lithuania Litas",
            "MOP": "Macau Pataca",
            "MKD": "Macedonia Denar",
            "MGA": "Madagascar Ariary",
            "MWK": "Malawi Kwacha",
            "MYR": "Malaysia Ringgit",
            "MVR": "Maldives (Maldive Islands) Rufiyaa",
            "MRO": "Mauritania Ouguiya",
            "MUR": "Mauritius Rupee",
            "MXN": "Mexico Peso",
            "MDL": "Moldova Leu",
            "MNT": "Mongolia Tughrik",
            "MAD": "Morocco Dirham",
            "MZN": "Mozambique Metical",
            "MMK": "Myanmar (Burma) Kyat",
            "NAD": "Namibia Dollar",
            "NPR": "Nepal Rupee",
            "ANG": "Netherlands Antilles Guilder",
            "NZD": "New Zealand Dollar",
            "NIO": "Nicaragua Cordoba",
            "NGN": "Nigeria Naira",
            "NOK": "Norway Krone",
            "OMR": "Oman Rial",
            "PKR": "Pakistan Rupee",
            "PAB": "Panama Balboa",
            "PGK": "Papua New Guinea Kina",
            "PYG": "Paraguay Guarani",
            "PEN": "Peru Nuevo Sol",
            "PHP": "Philippines Peso",
            "PLN": "Poland Zloty",
            "QAR": "Qatar Riyal",
            "RON": "Romania New Leu",
            "RUB": "Russia Ruble",
            "RWF": "Rwanda Franc",
            "SHP": "Saint Helena Pound",
            "WST": "Samoa Tala",
            "STD": "São Tomé and Príncipe Dobra",
            "SAR": "Saudi Arabia Riyal",
            "SPL": "Seborga Luigino",
            "RSD": "Serbia Dinar",
            "SCR": "Seychelles Rupee",
            "SLL": "Sierra Leone Leone",
            "SGD": "Singapore Dollar",
            "SBD": "Solomon Islands Dollar",
            "SOS": "Somalia Shilling",
            "ZAR": "South Africa Rand",
            "LKR": "Sri Lanka Rupee",
            "SDG": "Sudan Pound",
            "SRD": "Suriname Dollar",
            "SZL": "Swaziland Lilangeni",
            "SEK": "Sweden Krona",
            "CHF": "Switzerland Franc",
            "SYP": "Syria Pound",
            "TWD": "Taiwan New Dollar",
            "TJS": "Tajikistan Somoni",
            "TZS": "Tanzania Shilling",
            "THB": "Thailand Baht",
            "TOP": "Tonga Pa'anga",
            "TTD": "Trinidad and Tobago Dollar",
            "TND": "Tunisia Dinar",
            "TRY": "Turkey Lira",
            "TMT": "Turkmenistan Manat",
            "TVD": "Tuvalu Dollar",
            "UGX": "Uganda Shilling",
            "UAH": "Ukraine Hryvna",
            "AED": "United Arab Emirates Dirham",
            "GBP": "United Kingdom Pound",
            "USD": "United States Dollar",
            "UYU": "Uruguay Peso",
            "UZS": "Uzbekistan Som",
            "VUV": "Vanuatu Vatu",
            "VEF": "Venezuela Bolivar",
            "VND": "Viet Nam Dong",
            "YER": "Yemen Rial",
            "ZMK": "Zambia Kwacha",
            "ZWD": "Zimbabwe Dollar"}

ISO_IBAN = {"AL": 28, "AD": 24, "AT": 20, "AZ": 28, "BE": 16, "BH": 22,
            "BA": 20, "BR": 29, "BG": 22, "CR": 21, "HR": 21, "CY": 28,
            "CZ": 24, "DK": 18, "DO": 28, "EE": 20, "FO": 18, "FI": 18,
            "FR": 27, "GE": 22, "DE": 22, "GI": 23, "GR": 27, "GL": 18,
            "GT": 28, "HU": 28, "IS": 26, "IE": 22, "IL": 23, "IT": 27,
            "KZ": 20, "KW": 30, "LV": 21, "LB": 28, "LI": 21, "LT": 20,
            "LU": 20, "MK": 19, "MT": 31, "MR": 27, "MU": 30, "MC": 27,
            "MD": 24, "ME": 22, "NL": 18, "NO": 15, "PK": 24, "PS": 29,
            "PL": 28, "PT": 25, "RO": 24, "SM": 27, "SA": 24, "RS": 22,
            "SK": 24, "SI": 19, "ES": 24, "SE": 24, "CH": 21, "TN": 24,
            "TR": 26, "AE": 23, "GB": 22, "VG": 24}


def memoise(function):
    cache = {}

    def memoised(*args):
        if args not in cache:
            cache[args] = function(*args)
        return cache[args]

    return memoised


def gather_every_nth(L, n):
    '''(list, int) -> list

    Return a new list containing every n'th element in L, starting at index 0.

    Precondition: n >= 1

    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)
    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
    ['a', 'c', 'e', 'g', 'i']
    '''

    result = []
    i = 0
    while i < len(L):
        result.append(L[i])
        i += n

    return result


def union_lists(list_one, list_two):
    """
    Returns the ordered union of two lists as a list
    list(set(list_one) | set(list_two)) would remove the order
    """
    items = []
    return [items.append(first) for first in list_one
            for second in list_two
            if second not in items]


def intersect_lists(list_one, list_two):
    """
    Returns the ordered intersection of two lists as a list
    list(set(list_one) & set(list_two)) would remove the order
    """
    return [first for first in list_one
            for second in list_two
            if first == second]


def remove_duplicates_from_list(the_list):
    dictionary = {}
    for item in the_list:
        print(dictionary, item)
        dictionary[item] = dictionary.has_key(item)
    return [keep for keep in dictionary.keys() if not dictionary[keep]]


def compare_values_of_list(the_list, the_item=0):
    list_length = len(the_list)
    if list_length == 1:
        return [-1]
    if list_length == 0:
        return [None]
    result_list = []
    for check_item in range(0, list_length):
        if the_item == check_item:
            result_list.append(-1)
        elif the_list[the_item] == the_list[check_item]:
            result_list.append(1)
        else:
            result_list.append(0)
    return result_list


def list2dict(keys, values):
    return {key: value for key, value in zip(keys, values)}


def dict2list(dictionary, keys):
    return [dictionary[keys[key]] for key in range(len(keys))]


def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    '''

    result = []
    for k in L:
        if k in d:
            result += [k]

    return result


def count_values_that_are_keys(d):
    '''(dict) -> int

    Return the number of values in d that are also keys in d.

    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 3})
    3
    >>> count_values_that_are_keys({1: 1})
    1
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
    2
    >>> count_values_that_are_keys({1: 2})
    0
    '''

    result = 0
    for k in d:
        if d[k] in d:
            result = result + 1

    return result


def flatten(root):
    if isinstance(root, (list, tuple)):
        for element in root:
            for e in flatten(element):
                yield e
    else:
        yield root


def linear_search(items, find):
    """
    >>> items = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> find = 'c'
    >>> linear_search (items, find)
    (True, 2)
    """
    position = 0
    finish = len(items)
    while position != finish:
        if items[position] == find:
            return True, position
        else:
            position += 1
    return False, -1


def binary_search(items, find):
    """
    >>> items = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> find = 'c'
    >>> binary_search (items, find)
    (True, 2)
    """
    position = 0
    finish = len(items) - 1
    while position <= finish:
        middle = (position + finish) // 2
        if items[middle] < find:
            position = middle + 1
        else:
            finish = middle - 1
    if position == len(items) or items[position] != find:
        return False, -1
    else:
        return True, position


def nested_list_search(structure, term):
    """
    >>> nested_list_search([1, (2, 3), 4, [5, [6 , [['x']], [8, 9]], -10]], 0)
    False
    >>> nested_list_search([1, (2, 3), 4, [5, [6 , [['x']], [8, 9]], -10]], 1)
    True
    >>> nested_list_search([1, (2, 3), 4, [5, [6 , [['x']], [8, 9]], -10]], 3)
    False
    >>> nested_list_search([1, (2, 3), 4, [5, [6 , [['x']], [8, 9]], -10]], 5)
    True
    >>> nested_list_search([1, (2, 3), 4, [5, [6 , [['x']], [8, 9]], -10]], 7)
    False
    >>> nested_list_search([1, (2, 3), 4, [5, [6 , [['x']], [8, 9]], -10]], 9)
    True
    >>> nested_list_search([1, (2, 3), 4, [5, [6 , [['x']], [8, 9]], -10]], 10)
    False
    """
    found = False
    # print ("Searching for", term, "in", structure)
    for item in structure:
        if type(item) == list:
            # print ("Inspecting", item)
            found = nested_list_search(item, term)
        # elif type(item) == type(term):
        #    #print ("Comparing", item, "with", term)
        #    found = (item == term)
        else:
            # print ("Checking", item, "with", term)
            found = (item == term)
        if found:
            return found
    # print ("Unable to find", term, "in", structure)
    return found


def nested_list_remove(structure, term):
    """
    Returns a structure of type list minus the search term
    """
    while nested_list_search(structure, term):  # Cheat using nested search
        # if structure != False:     # Flawed with self([6, [6], 6, [6]], 6)
        for item in structure:
            if type(item) == list:
                nested_list_remove(item, term)
            while term in structure:
                for position in range(len(structure), 0, -1):
                    if structure[position - 1] == term:
                        structure.pop(position - 1)
    return structure


def nested_list_replace(structure, term, replace):
    """
    Returns a structure of type list minus the search term
    """
    # Nothing to do
    if term == replace:
        # print (term, "is the same as", replace)
        return structure

    # Avoids recursion
    if type(replace) == list:
        if term in replace:
            recursion = ((str(term) + "…"))
            for repeat in range(len(replace)):
                if replace[repeat] == term:
                    # print ("Replacing", term, "with", recursion)
                    replace[repeat] = recursion

    if structure != False:
        for item in structure:
            if type(item) == list:
                nested_list_replace(item, term, replace)
            while term in structure:
                for position in range(len(structure)):
                    if structure[position] == term:
                        # print ("Replacing", term, "in", structure, "with", replace)
                        structure[position] = replace
    # print (structure)
    return structure


def duplicate_search(items):
    length = len(items)
    for compare in range(length):
        for seek in range(compare + 1, length):
            if items[seek] == items[compare]:
                return True, items[seek]
    return False, -1


def bubblesort(array):
    """
    >>> items = ['g', 'a', 'b', 'c', 'h', 'd', 'e', 'f']
    >>> bubblesort (items)
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """
    "Sorts array in place and returns it."
    for passes_left in range(len(array) - 1, 0, -1):
        for index in range(passes_left):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
    return array


def bubble_sort(array):
    """
    >>> items = ['g', 'a', 'b', 'c', 'h', 'd', 'e', 'f']
    >>> bubble_sort (items)
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """
    last = len(array) - 1
    while last != 0:
        for index in range(last):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
        last -= 1
    return array


def selection_sort(array):
    """
    >>> items = ['g', 'a', 'b', 'c', 'h', 'd', 'e', 'f']
    >>> selection_sort (items)
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """

    def lowest(array, index, length):
        smallest = index
        # length = len(array)
        for index in range(index + 1, length):
            if array[index] < array[smallest]:
                smallest = index
        return smallest

    length = len(array)
    for index in range(length):
        # print (array)
        smallest = lowest(array, index, length)
        array[smallest], array[index] = array[index], array[smallest]
    return array


def insertsort(array):
    """
    >>> items = ['g', 'a', 'b', 'c', 'h', 'd', 'e', 'f']
    >>> insertsort (items)
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """
    for removed_index in range(1, len(array)):
        removed_value = array[removed_index]
        insert_index = removed_index
        # print (array)
        while insert_index > 0 and array[insert_index - 1] > removed_value:
            array[insert_index] = array[insert_index - 1]
            insert_index = insert_index - 1
        array[insert_index] = removed_value
    return array


def insert_sort(array):
    """
    >>> items = ['g', 'a', 'b', 'c', 'h', 'd', 'e', 'f']
    >>> insert_sort (items)
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """

    def insert(array, index):
        value = array[index]
        seek = index
        while seek != 0 and array[seek - 1] > value:
            array[seek] = array[seek - 1]
            seek -= 1
        array[seek] = value

    length = len(array)
    for index in range(length):
        # print (array)
        insert(array, index)
    return array


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    print(result)
    return result


def merge_sort(array):
    if len(array) <= 1:
        return array
    # print (array)
    middle = int(len(array) / 2)
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)


def quick_sort(array):
    if array == []:
        return array
    # print (array)
    if len(array) == 1:
        return array
    return quick_sort([x for x in array[1:] if x < array[0]]) + array[0:1] + \
           quick_sort([x for x in array[1:] if x >= array[0]])


def quicksort(array):
    return ((quicksort([x for x in array[1:] if x < array[0]]) + array[0:1] + \
             quicksort([x for x in array[1:] if x >= array[0]]))
            if array else [])


# With in place partitioning and random pivot selection:
def _doquicksort(array, left, right):
    """Quick sort"""

    def partition(array, left, right, pivotindex):
        """In place paritioning from left to right using the element at
        pivotindex as the pivot. Returns the new pivot position."""

        pivot = array[pivotindex]
        # swap pivot and the last element
        array[right], array[pivotindex] = array[pivotindex], array[right]

        storeindex = left
        for index in range(left, right):
            print(array)
            if array[index] < pivot:
                array[index], array[storeindex] = array[storeindex], array[index]
                storeindex += 1

        # move pivot to the proper place
        array[storeindex], array[right] = array[right], array[storeindex]
        return storeindex

    if right > left:
        # random pivot
        # pivotindex = random.randint(left, right)
        pivotindex = partition(array, left, right, random.randint(left, right))
        _doquicksort(array, left, pivotindex)
        _doquicksort(array, pivotindex + 1, right)

    return array


def quicksorting(array):
    return _doquicksort(array, 0, len(array) - 1)


inversions = 0
comparisons = 0


def swap(array, a, b):
    global inversions
    array[a], array[b] = array[b], array[a]
    inversions += 1


def partition(array, start, end):
    global comparisons
    left = start + 1
    pivot = array[start]
    for right in range(start + 1, end):
        comparisons += 1
        if pivot > array[right]:
            swap(array, left, right)
            left = left + 1
    swap(array, start, left - 1)
    return left - 1


def quickSortHelper(array, start, end):
    if start < end:
        splitPoint = partition(array, start, end)
        quickSortHelper(array, start, splitPoint)
        quickSortHelper(array, splitPoint + 1, end)


def quickSorter(array):
    quickSortHelper(array, 0, len(array))
    print(inversions)
    print(comparisons)
    return array


def neighbours(points):
    assert isinstance(points, object)   # Inserted by PyCharm
    x, y = points
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1
    yield x + 1, y + 1
    yield x + 1, y - 1
    yield x - 1, y + 1
    yield x - 1, y - 1


def advance(board):
    newstate = set()
    recalc = board | set(itertools.chain(*map(neighbours, board)))
    for point in recalc:
        count = sum((neigh in board)
                    for neigh in neighbours(point))
        if count == 3 or (count == 2 and point in board):
            newstate.add(point)
    return newstate


glider = set([(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)])
for i in range(1000):
    glider = advance(glider)
print(glider)


def valid_iban(iban):
    """
    >>> iban_tests = ["GB82 WEST 1234 5698 7654 32", "GB82 TEST 1234 5698 7654 32"]
    >>> for account in iban_tests: print('%s validation is: %s' % (account, valid_iban(account)))
    GB82 WEST 1234 5698 7654 32 validation is: True
    GB82 TEST 1234 5698 7654 32 validation is: False
    """
    # Ensure upper alphanumeric input.
    iban = iban.replace(' ', '').replace('\t', '')
    if not re.match(r'^[\dA-Z]+$', iban):
        return False
    # Validate country code against expected length.
    if len(iban) != ISO_IBAN[iban[:2]]:
        return False
    # Shift and convert.
    iban = iban[4:] + iban[:4]
    digits = int(''.join(str(int(ch, 36)) for ch in iban))  # BASE 36: 0..9,A..Z -> 0..35
    return digits % 97 == 1


def check_bitcoin(bitcoin):
    """
    >>> bitcoin = '1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i'
    >>> check_bitcoin(bitcoin)
    True
    >>> check_bitcoin( bitcoin.replace('N', 'P', 1) )
    False
    >>> check_bitcoin('1111111111111111111114oLvT2')
    True
    >>> check_bitcoin("17NdbrSGoUotzeGCcMMCqnFkEvLymoou9j")
    True
    """

    def decode_base58(bitcoin, length):
        digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

        n = 0
        for char in bitcoin:
            n = n * 58 + digits58.index(char)
        return n.to_bytes(length, 'big')

    bcbytes = decode_base58(bitcoin, 25)
    return bcbytes[-4:] == hashlib.sha256(hashlib.sha256(bcbytes[:-4]).digest()).digest()[:4]


def zero_vector(domain):
    return Vector(domain, {element: 0 for element in domain})


def setitem(vector, domain, value):
    vector.element[domain] = value


def getitem(vector, domain):
    return vector.element[domain] if domain in vector.element else 0


def list2vector(L):
    # Vec(set(range(len(L))), {k: x for k, x in enumerate(L) } )
    # Vec(set(range(len(L))), {k: x for k, x in range(len(L) ) } )
    return Vector(v, {e for e in range(len(L) - 1)})


class Stack:
    """Stack of objects; Last In First Out basis"""

    def __init__(self, stackList=[]):
        "Initialise the stack"
        self.stackList = stackList

    def push(self, obj):
        "Add obj to top of stack"
        self.stackList.append(obj)
        return True

    def top(self):
        "Return topmost element"
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stackList[-1]

    def pop(self):
        "Return and remove topmost element"
        if self.isEmpty():
            return "Unable to pop: Stack is empty"
        else:
            return self.stackList.pop()

    def isEmpty(self):
        "Return truthvalue of Stack's emptiness"
        return len(self.stackList) == 0

    def isFull(self):
        "Return truthvalue of Stack's fullness"
        return False

    def clear(self):
        "Remove all elements from Stack"
        self.stackList[:] = []
        return True

    def length(self):
        "Returns the length of the Stack"
        return len(self.stackList)

    def display(self):
        "Display the Stack"
        print(self.stackList)
        return True

    def __del__(self):
        "Terminate the stack"
        return ()


class Queue:
    """Queue of Objects; First In First Out basis"""

    def __init__(self, queueList=[]):
        "Initialise the queue"
        self.queueList = queueList

    def enqueue(self, obj):
        "Add element to Queue"
        self.queueList.append(obj)
        return True

    def dequeue(self):
        "Return and remove first element from Queue"
        if (self.isEmpty()):
            return "Unable to dequeue: Queue is empty"
        else:
            obj = self.queueList[0]
            self.queueList = self.queueList[1:]
            return obj

    def isEmpty(self):
        "Return truthvalue of Queue's emptiness"
        return len(self.queueList) == 0

    def isFull(self):
        "Return truthvalue of Queue's fullness"
        return False

    def clear(self):
        "Remove all elements from Queue"
        self.queueList[:] = []
        return True

    def putFront(self, obj):
        "Adds element to front of Queue"
        self.queueList.insert(0, obj)
        return True

    def getRear(self):
        "Returns and removes the last element in the Queue"
        if self.isEmpty():
            return "Unable to getRear: Stack is empty"
        else:
            return self.queueList.pop()

    def length(self):
        "Returns the length of the Queue"
        return len(self.queueList)

    def display(self):
        "Display the Queue"
        print(self.queueList)
        return True

    def __del__(self):
        "Terminate the queue"
        return ()


class Tree(object):
    """A tree with internal values."""

    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

    def __repr__(self):
        args = repr(self.entry)
        if self.left or self.right:
            args += ', {0}, {1}'.format(repr(self.left), repr(self.right))
        return 'Tree({0})'.format(args)


def count_entries(tree):
    """Return the number of entries in a Tree."""
    if tree is None:
        return 0
    return 1 + count_entries(tree.left) + count_entries(tree.right)


@memoise
def fibonacci_tree(number):
    """Return a Tree that represents a recursive Fibonacci calculation.

    >>> fibonacci_tree(3)
    Tree(1, Tree(0), Tree(1))
    """
    if number == 1:
        return Tree(0)
    if number == 2:
        return Tree(1)
    left = fibonacci_tree(number - 2)
    right = fibonacci_tree(number - 1)
    return Tree(left.entry + right.entry, left, right)


class ObjectClass(object):
    """Generic object"""

    def __init__(self, instance):
        self.instance = instance

    def ObjectMethod(self):
        'Comments for the method object'
        print("A method of ObjectClass has been invoked")


class SubObjectClass(ObjectClass):
    """Inherit the properties of ObjectClass"""

    def __init__(self, subInstance):
        self.instance = subInstance

    def ObjectMethod(self):
        'Override the method of the parent'
        print("A method of SubObjectClass has overridden the parent method")
        print("SubObjectClass is a child object of ObjectClass")


class SuperObjectClass(ObjectClass):
    """Inherit the properties of ObjectClass"""

    def __init__(self, superInstance):
        self.instance = superInstance

    def ObjectMethod(self):
        'Override the method of the parent'

        super(SuperObjectClass, self).ObjectMethod()
        print("by the method of SuperObjectClass, which depends on it")


# If this module is being run as a stand-alone program
import doctest

if __name__ == '__main__':
    doctest.testmod()
    unittest.main(exit=False)

##    items = list(currency.values())
##    cProfile.run('bubblesort (items)')
##    items = list(currency.values())
##    cProfile.run('bubble_sort (items)')
##    items = list(currency.values())
##    cProfile.run('selection_sort (items)')
##    items = list(currency.values())
##    cProfile.run('insertsort (items)')
##    items = list(currency.values())
##    cProfile.run('insert_sort (items)')
##    items = list(currency.values())
##    cProfile.run('qsort (items)')
##    items = list(currency.values())
##    cProfile.run('quicksort (items)')


##    print (__doc__)
##    
##    print ("\nSTACK class info:")
##    print (Stack.__doc__)
##    print (help (Stack) )
##    info(Stack())
##    
##    print ("\nQUEUE class info:")
##    print (Queue.__doc__)
##    print (help (Queue) )
##    info(Queue())		
##
##    print ("\nTREE class info:")
##    print (Tree.__doc__)
##    print (help (Tree) )
##    info(Tree())
