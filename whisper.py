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

import binascii
import cryptography
import hashlib
import bcrypt
import doctest
import keyword
import math
import pgpy
import os
import nacl
import ssl
import random
import sys
import rsa
import unittest
import uuid
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

import maths, ropes

ENCRYPT, DECRYPT = 1, -1

CEASAR_CIPHER = {
    "00": (
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"),
    "01": (
    "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A"),
    "02": (
    "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B"),
    "03": (
    "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C"),
    "04": (
    "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
    "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D"),
    "05": (
    "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
    "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E"),
    "06": (
    "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
    "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F"),
    "07": (
    "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G"),
    "08": (
    "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H"),
    "09": (
    "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
    "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I"),
    "10": (
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
    "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"),
    "11": (
    "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
    "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"),
    "12": (
    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
    "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"),
    "13": (
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"),
    "14": (
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A",
    "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"),
    "15": (
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B",
    "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"),
    "16": (
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C",
    "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"),
    "17": (
    "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D",
    "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"),
    "18": (
    "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"),
    "19": (
    "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F",
    "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S"),
    "20": (
    "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"),
    "21": (
    "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H",
    "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"),
    "22": (
    "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I",
    "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"),
    "23": (
    "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"),
    "24": (
    "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
    "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"),
    "25": (
    "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y")}

CEASAR = {0: tuple([chr(character) for character in range (65, 91)])}
#for letter in range(1, 26):
#    CEASAR[letter] = tuple([])
#for letter in range(26):
#    CEASAR[letter] = tuple([ (  (letter + character) % 91 )
#                             if letter
#                            for character in range(65, 91)])


ROT13_SHIFT = CEASAR_CIPHER['13']


def memoise(function):
    cache = {}

    def memoised(*args):
        if args not in cache:
            cache[args] = function(*args)
        return cache[args]

    return memoised


def load_dictionary():
    dictionary_file = open(r"""G:\WorkingData\Work @ Home\Python3\Python Examples\dictionary.txt""")
    english_words = {}
    for word in dictionary_file.read().split('\n'):
        english_words[word] = None
    dictionary_file.close()
    return english_words


ENGLISH_WORDS = load_dictionary()

# EN_ALPHABET_LOWER = """abcdefghijklmnopqrstuvwxyz""" # ASCII 97 - 122
# EN_ALPHABET_UPPER = """ABCDEFGHIJKLMNOPQRSTUVWXYZ""" # ASCII 65 - 90
# EN_LETTERS_AND_SPACE = ALPHABET_UPPER + ALPHABET_LOWER + ' \t\n'
EN_LETTER_FREQUENCY = "eta"
EN_PAIRS_FREQUENCY = ['he', 'an', 'in', 'th']


def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0  # no words at all, so return 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in ropes.ASCII_CHARACTERS:
            lettersOnly += [symbol]
    return ''.join(lettersOnly)


def is_English(message, wordPercentage=20, letterPercentage=85):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch


"""
Access Control
    Confidentiality from unintended disclosure
    Integrity from unauthorised alternation
    Availablity by preventing destruction

Identification
    Enter username:

Authentication
    Prove identification claim
    First factor
    Enter password:
    Second factor
    Enter passcode:
    Swipe card
    Answer question
    Scan iris or fingerprint

Authorisation
    Permissions to resources
    Read
    Create
    Update
    Delete

Accountability
    Logging activity
    Auditing historical logs
    Monitoring activity
    Alerting
    Reporting
"""


def shift_alphabet(mode, string, key):  # AKA Ceasar

    if mode == DECRYPT:
        key = -key

    alphabet_size = len(ropes.ALPHABET_LOWER)
    translation = ''

##    for character in string:
##        if character.isalpha():
##            if character.isupper():
##                translation += chr((((ord(character) - 65) - key) % 26) + 65)
##            elif character.islower():
##                translation += chr((((ord(character) - 97) - key) % 26) + 97)
##            elif character.isdigit():
##                translation += chr((((ord(character) - 48) - key) % 10) + 48)
##        else:
##            translation += character

    for character in string:
        if character.isalpha():
            replacement = ord(character) + key
            if character.isupper():
                if replacement > ord('Z'):
                    replacement -= alphabet_size
                elif replacement < ord('A'):
                    replacement += alphabet_size
            elif character.islower():
                if replacement > ord('z'):
                    replacement -= alphabet_size
                elif replacement < ord('a'):
                    replacement += alphabet_size
##            elif character.isdigit():
##                if replacement > ord('9'):
##                    replacement -= 10
##                elif replacement < ord('0'):
##                    replacement += 10
            translation += chr(replacement)
        else:
            translation += character

    return translation


##def rotate_alphabet(mode, string, key):  #AKA Ceasar
##    if mode == DECRYPT:
##        key = -key
##    return string.translate(str.maketrans(
##        string.ascii_uppercase + string.ascii_lowercase,
##        string.ascii_uppercase[key:] + string.ascii_uppercase[:key] +
##        string.ascii_lowercase[key:] + string.ascii_lowercase[:key] ) )

def encrypt_shift(source, key):
    return shift_alphabet(ENCRYPT, source, key)


def decrypt_shift(source, key):
    return shift_alphabet(DECRYPT, source, key)


def rotate_thirteen(source):
    return shift_alphabet(DECRYPT, source, 13)


def reverse_shift(source):
    return ropes.reverse_string(rotate_thirteen(source))


def brute_force_shaft(source):
    return [is_English(decrypt_shift(source, key))
            for key in range(len(ropes.ALPHABET_LOWER))].index(True)


def randomise():
    random.seed(os.urandom
                (int(random.random() *
                     random.randint(11111, 99999))))


def lcg_repeat(possible_values, sample_size):
    # These intermediate results are exceedingly large numbers;
    # Python automatically starts using bignums behind the scenes.
    numerator = math.factorial(possible_values)
    denominator = (possible_values ** sample_size) * math.factorial(possible_values - sample_size)
    # Now we need to get from bignums to floats without intermediate
    # values too large to cast into a double.  Taking the logs and
    # subtracting them is equivalent to division.
    log_prob_no_pair = math.log10(numerator) - math.log10(denominator)
    # We've just calculated the log of the probability that *NO*
    # two matching pairs occur in the sample.  The probability
    # of at least one collision is 1.0 - the probability that no
    # matching pairs exist.
    return 1.0 - (10 ** log_prob_no_pair)


def lcg_random(factor, constant, modulate, previous):
    return (factor * previous + constant) % modulate


def uuid_random():
    return uuid.uuid4()


def supply_key():
    randomise()
    while True:
        div_key = random.randint(2, len(ropes.ASCII_CHARACTERS))
        mod_key = random.randint(2, len(ropes.ASCII_CHARACTERS))
        if maths.euclid_gcd(div_key, len(ropes.ASCII_CHARACTERS)) != 1:
            return div_key * len(ropes.ASCII_CHARACTERS) + mod_key


def secret_keys(key):
    div_key = key // len(ropes.ASCII_CHARACTERS)
    mod_key = key % len(ropes.ASCII_CHARACTERS)
    return (div_key, mod_key)


def secure_keys(div_key, mod_key, mode):
    if div_key == 1 and mode == ENCRYPT:
        return False, 'The affine cipher becomes incredibly weak when the div_key is set to 1. Choose a different key.'
    if mod_key == 0 and mode == ENCRYPT:
        return False, 'The affine cipher becomes incredibly weak when the mod_key is set to 0. Choose a different key.'
    if div_key < 0 or mod_key < 0 or mod_key > len(ropes.ASCII_CHARACTERS) - 1:
        return False, 'The div_key must be greater than 0 and the mod_key must be between 0 and %s.' % (
        len(ropes.ASCII_CHARACTERS) - 1)
    if maths.euclid_gcd(div_key, len(ropes.ASCII_CHARACTERS)) != 1:
        return False, 'The div_key (%s) and the character set size (%s) are not relatively prime. Choose a different key.' % (
        div_key, len(ropes.ASCII_CHARACTERS))
    return True, 'The key combination does not comprimise the strength of the affine cipher'


def encrypt_affine(key, plaintext):
    div_key, mod_key = secret_keys(key)
    result, message = secure_keys(div_key, mod_key, ENCRYPT)
    if result == False:
        return result, message

    ciphertext = ''
    for character in plaintext:
        if character in ropes.ASCII_CHARACTERS:
            # encrypt this character
            character_index = ropes.ASCII_CHARACTERS.find(character)
            ciphertext += ropes.ASCII_CHARACTERS[(character_index *
                                                  div_key + mod_key) %
                                                 len(ropes.ASCII_CHARACTERS)]
        else:
            ciphertext += character  # just append original non-ascii character
    return result, ciphertext


def decrypt_affine(key, ciphertext):
    div_key, mod_key = secret_keys(key)
    result, message = secure_keys(div_key, mod_key, DECRYPT)
    if result == False:
        return result, message

    plaintext = ''
    mod_inv_div_key = maths.modular_inverse(div_key, len(ropes.ASCII_CHARACTERS))

    for character in ciphertext:
        if character in ropes.ASCII_CHARACTERS:
            # decrypt this character
            character_index = ropes.ASCII_CHARACTERS.find(character)
            plaintext += ropes.ASCII_CHARACTERS[(character_index - mod_key) *
                                                mod_inv_div_key %
                                                len(ropes.ASCII_CHARACTERS)]
        else:
            plaintext += character  # just append original non-ascii character
    return result, plaintext


def brute_force_affine(ciphertext, key=1):
    # brute-force by looping through every possible key
    for key in range(key, len(ropes.ASCII_CHARACTERS) ** 2):
        div_key = secret_keys(key)[0]
        if maths.euclid_gcd(div_key, len(ropes.ASCII_CHARACTERS)) != 1:
            continue

        decrypt_attempt = decrypt_affine(key, ciphertext)[1]

        if is_English(decrypt_attempt):
            return key, decrypt_attempt
    return None


def valid_scramble_key(key):
    return list(key.upper()).sort() == list(ropes.ALPHABET_UPPER).sort()


def build_scramble_key():
    randomise()

    key = list(ropes.ALPHABET_UPPER)
    random.shuffle(key)
    return ''.join(key)


def scramble_alphabet(mode, plaintext, key):  # AKA Subsitution cipher
    translation = ''
    sorting_key = ropes.ALPHABET_UPPER
    shuffle_key = key
    if mode == DECRYPT:  # Swap keys for unscrambling
        sorting_key, shuffle_key = shuffle_key, sorting_key

    # loop through each character in the string
    for character in plaintext:
        if character.upper() in sorting_key:
            # encrypt/decrypt the character
            swapkey_index = sorting_key.find(character.upper())
            if character.isupper():
                translation += shuffle_key[swapkey_index].upper()
            else:
                translation += shuffle_key[swapkey_index].lower()
        else:
            # character is not in LETTERS, just add it
            translation += character
    return translation


def encrypt_scrambler(plaintext, key):
    if valid_scramble_key(key):
        return scramble_alphabet(ENCRYPT, plaintext, key)


def decrypt_scrambled(ciphertext, key):
    return scramble_alphabet(DECRYPT, ciphertext, key)


def multi_shift_askey(mode, string, key):  # AKA Vigener
    translation = []  # stores the encrypted/decrypted string

    key_index = 0

    for character in string:  # loop through each character in string
        key_shift = ropes.ASCII_CHARACTERS.find(character)
        if key_shift != -1:  # -1 means character was not found in ropes.ASCII_CHARACTERS
            if mode == ENCRYPT:
                key_shift += ropes.ASCII_CHARACTERS.find(key[key_index])  # add if encrypting
            elif mode == DECRYPT:
                key_shift -= ropes.ASCII_CHARACTERS.find(key[key_index])  # subtract if decrypting

            key_shift %= len(ropes.ASCII_CHARACTERS)  # handle the potential wrap-around
            translation.append(ropes.ASCII_CHARACTERS[key_shift])

            key_index += 1  # move to the next letter in the key
            if key_index == len(key):
                key_index = 0
        else:
            # The character was not in ropes.ASCII_CHARACTERS, so add it to translation as is.
            translation += [character]

    return ''.join(translation)


def encrypt_multi_shift(plaintext, key):
    return multi_shift_askey(ENCRYPT, plaintext, key)


def decrypt_multi_shift(ciphertext, key):
    return multi_shift_askey(DECRYPT, ciphertext, key)


def digitally_sign(source, secret, hasher="md5"):
    """
    >>> digitally_sign("Supercalifragilisticexpialidocious", 'pop song')
    ('Supercalifragilisticexpialidocious44bf69fb4ac3af50432043ab0f69aaaf', 16)
    """
    hasher = hasher.lower()
    if hasher == "sha512":
        secured = hashlib.sha512()
    elif hasher == "sha384":
        secured = hashlib.sha384()
    elif hasher == "sha256":
        secured = hashlib.sha256()
    elif hasher == "sha224":
        secured = hashlib.sha224()
    elif hasher == "sha1":
        secured = hashlib.sha1()
    elif hasher == "ripemd160":
        secured = hashlib.ripemd160()
    else:
        secured = hashlib.md5()

    secured.update(source.encode('utf-8') + secret.encode('utf-8'))
    digest = secured.hexdigest()
    return source + digest, secured.digest_size


def split_signed(signed, digest_size):
    """
    >>> split_signed('Supercalifragilisticexpialidocious44bf69fb4ac3af50432043ab0f69aaaf', 16)
    ('Supercalifragilisticexpialidocious', '44bf69fb4ac3af50432043ab0f69aaaf')
    """
    source = signed[: -digest_size * 2]
    digest = signed[-digest_size * 2:]
    return source, digest


def check_intregity(signed, secret, digest_size, hasher="md5"):
    source, digest = split_signed(signed, digest_size)
    print("source: ", source)
    print("digest: ", digest)
    return (signed, digest_size) == digitally_sign(source, secret, hasher)


def test_signing(hasher="sha512"):
    source = "Supercalifragilisticexpialidocious"
    secret = 'pop song'
    signed, digest_size = digitally_sign(source, secret, hasher)
    print("source: ", source)
    print("secret: ", secret)
    print("signed: ", signed)
    print("length: ", digest_size)
    return check_intregity(signed, secret, digest_size, hasher)


def parity():
    """
    Detect odd number of errors
    """
    return parity_bit


def checksum(par):
    """
    16bit checksum against a packet of data
    """
    return check_sum


def CRC32(message):
    """

    """
    return hex(binascii.crc32(message))


def ECC():
    """

    """
    return


def hamming():
    """

    """
    return


def LDPC():
    """

    """
    return


def reed_solomon():
    """

    """
    return


def hash_string(phrase, size = 128):
    _list = []
    for character in phrase:
        _list.append(ord(character))
        print (f"{character} == {_list[-1]}")
    return (sum(_list) % size)


def hash_fraction(m, n):
    """Compute the hash of a rational number m / n.

    Assumes m and n are integers, with n positive.
    Equivalent to hash(fractions.Fraction(m, n)).

    """
    P = sys.hash_info.modulus
    # Remove common factors of P.  (Unnecessary if m and n already coprime.)
    while m % P == n % P == 0:
        m, n = m // P, n // P

    if n % P == 0:
        hash_ = sys.hash_info.inf
    else:
        # Fermat's Little Theorem: pow(n, P-1, P) is 1, so
        # pow(n, P-2, P) gives the inverse of n modulo P.
        hash_ = (abs(m) % P) * pow(n, P - 2, P) % P
    if m < 0:
        hash_ = -hash_
    if hash_ == -1:
        hash_ = -2
    return hash_


def hash_float(x):
    """Compute the hash of a float x."""

    if math.isnan(x):
        return sys.hash_info.nan
    elif math.isinf(x):
        return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
    else:
        return hash_fraction(*x.as_integer_ratio())


def hash_complex(z):
    """Compute the hash of a complex number z."""

    hash_ = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
    # do a signed reduction modulo 2**sys.hash_info.width
    M = 2 ** (sys.hash_info.width - 1)
    hash_ = (hash_ & (M - 1)) - (hash & M)
    if hash_ == -1:
        hash_ == -2
    return hash_


# If this module is being run as a stand-alone program
import doctest

if __name__ == '__main__':
    doctest.testmod()
    unittest.main(exit=False)

    import this

    print(digitally_sign(rotate_thirteen(this.s), str(this.c), "sha512"))
