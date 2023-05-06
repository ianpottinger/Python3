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

import re   # regexr.com
import keyword
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


REGEX = 'Regular Expression'


import fileman


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def check_email(email):
    reg = r'^(((([a-z\d][\.\-\+_]?)*)[a-z0-9])+)\@(((([a-z\d][\.\-_]?){0,62})[a-z\d])+)\.([a-z\d]{2,6})$'
    return re.match(reg, email, re.IGNORECASE)


def is_valid_email(email):
    regex = r'^[\w.|-]+@(?:[\w.|-]{2,63}\.)+[a-z]{2,6}$'
    return bool(re.match(regex, email))


def valid_ip(ip_address):
    val_0_to_255 = r"(25[012345]|2[01234]\d|[01]?\d\d?)"
    pattern = "^(" + val_0_to_255 + r"\." + val_0_to_255 + r"\." + val_0_to_255 + r"\." + val_0_to_255 + r")$"
    return bool(re.match(pattern, ip_address))


def is_valid_ip_address(ip_address):
    regex = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$'
    return bool(re.match(regex, ip_address))


def is_valid_mac_address(mac_address):
    regex = r'^[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}$'
    return bool(re.match(regex, mac_address))



def is_valid_number(number):
    regex = r'^[-+]?(?:\b[0-9]+(?:\.[0-9]*)?|\.[0-9]+\b)(?:[eE][-+]?[0-9]+\b)?$'
    return bool(re.match(regex, number))


def is_valid_ssn(ssn):
    regex = r'^(?!000)([0-6]\d{2}|7([0-6]\d|7[012]))([ -]?)(?!00)\d\d\3(?!0000)\d{4}$'
    return bool(re.match(regex, ssn))


def is_valid_iso_date(date):
    regex = r'^((18|19|20)\d\d)-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])$'
    return bool(re.match(regex, date))


def check_date(date):
    seperator = r"[\/\-\.]"
    pattern = r"^(((0?[1-9]|1\d|2[0-8])" + seperator + r"(0?[1-9]|1[012])|(29|30)" + seperator + r"(0?[13456789]|1[012])|31" + seperator + r"(0?[13578]|1[02]))" + seperator + r"(19|[2-9]\d)\d{2}|29" + seperator + r"0?2" + seperator + r"((19|[2-9]\d)(0[48]|[2468][048]|[13579][26])|(([2468][048]|[3579][26])00)))$"
    return bool(re.match(pattern, date))


def valid_name(username):
    return bool(re.match(r"^[a-z][\da-z_]{6,22}[a-z\d]$", username, re.IGNORECASE))


# Match a UK format phone number
def match_uk_phone_number(number):
    # UK Phone numbers are 10 or 11 digits long, and have a 3, 4, 5 or 6 digit area code
    s = "(([ \-\.])*)?"
    pattern = r'^((\(?0\d{3}\)?' + s + r'\d{7,8})|(\(?0\d{4}\)?' + s + r'\d{6,7})|(\(?0\d{5}\)?' + s + r'\d{5,6})|(\(?0\d{6}\)?' + s + r'\d{4,5}))$'
    result = re.match(pattern, number)
    return bool(result)


def match_uk_national_insurance(ni):
    digits_1_and_2 = "[ABCEGHJKLMNOPRSTWXYZ][ABCEGHJKLMNPRSTWXYZ]"  
    the_rest = "\d{6}[A-D]?"
    reg = "^" + digits_1_and_2 + the_rest + "$"
    return bool(re.match(reg, ni))


def is_valid_license_plate(plate):
    """
    Returns True if the given license plate is valid according to DVLA format.
    """
    pattern = r'^[A-Z]{2}\d{2}\s?[A-Z]{3}$'
    return bool(re.match(pattern, plate))


plate = 'AB12 CDE'
if is_valid_license_plate(plate):
    print('Valid license plate')
else:
    print('Invalid license plate')


def validate_uk_driving_license(license_number):
    """
    Validate a UK driving license number using a regular expression.

    Args:
        license_number (str): the driving license number to be validated

    Returns:
        bool: True if the license number is valid, False otherwise
    """

    # Define the regular expression pattern to match a UK driving license number
    pattern = r"^(?!^.{21,}$)(?:[A-Z]|[A-Z]{2})(?:[0-9]{6})(?:[0-9]|[A-Z]){2}[0-9]{2}$"

    # Use the re.match() function to test if the license number matches the pattern
    if re.match(pattern, license_number):
        return True
    else:
        return False


def is_valid_uk_passport(passport_number):
    regex = r"^([0-9]{9}|[0-9]{3}[A-Z][0-9]{6})$"
    return bool(re.match(regex, passport_number))


passport_number = "123456789"
if is_valid_uk_passport(passport_number):
    print(f"{passport_number} is a valid UK passport number")
else:
    print(f"{passport_number} is not a valid UK passport number")


def match_us_phone(number):
    reg = r"^\(?\d{3}\)?[\s\.-]?\d{3}[\s\.-]?\d{4}$"
    return bool(re.match(reg, number))


# Match a US social security number
def match_us_social_security(ss_num):
    return bool(re.match(r'\d{3}-\d{2}-\d{4}', ss_num))


def replace_urls(string):
    host = r'([a-z\d][-a-z\d]*[a-z\d]\.)+[a-z][-a-z\d]*[a-z]'
    port = r'(:\d{1,})?'
    path = r'(\/[^?<>\#\"\s]+)?'
    query = r'(\?[^<>\#\"\s]+)?'
    return re.sub(rf'((ht|f)tps?:\/\/{host}{port}{path}{query})', r'<a href="\g<1>">\g<1></a>', string, flags=re.IGNORECASE)


def BBcode(string):
    # get rid of all HTML tags
    string = re.sub(r'<[^>]*>', '', string)
    
    patterns = {
        "bold": r'\[b\](.*?)\[/b\]',
        "italics": r'\[i\](.*?)\[/i\]',
        "underline": r'\[u\](.*?)\[/u\]',
        "link_title": r'\[url=(.*?)](.*?)\[/url\]',
        "link_basic": r'\[url](.*?)\[/url\]',
        "color": r'\[color=(red|green|blue|yellow)\](.*?)\[/color\]',
    }

    replacements = {
        "bold": r'<b>\g<1></b>',
        "italics": r'<i>\g<1></i>',
        "underline": r'<u>\g<1></u>',
        "link_title": r'<a href="\g<1>">\g<2></a>',
        "link_basic": r'<a href="\g<1>">\g<1></a>',
        "color": r'<span style="color:\g<1>;">\g<2></span>',
    }

    for pattern_name, pattern in patterns.items():
        string = re.sub(pattern, replacements[pattern_name], string, flags=re.IGNORECASE)

    return string


def cleanTags(source, tags=None):
    def clean(matched):
        attribs = r"javascript:|onclick|ondblclick|onmousedown|onmouseup|onmouseover|" \
                  r"onmousemove|onmouseout|onkeypress|onkeydown|onkeyup|" \
                  r"onload|class|id|src|style"
        quot = r'"|\'|\`'
        stripAttrib = rf"' ({attribs})\s*=\s*({quot})(.*?)(\2)'i"
        clean = re.sub(stripAttrib, '', matched.group(0))
        return clean

    allowedTags = '<a><br><b><i><br><li><ol><p><strong><u><ul>'
    clean = re.sub(rf'<(?!{allowedTags})([^>]+)>', clean, source, flags=re.IGNORECASE)
    return clean
    

def deswear(string):
    def prep_regexp_array(item):
        item = rf"({re.escape(item)})"
        return item

    def stars(matches):
        return matches[0][0] + '*' * (len(matches[0]) - 1)
        
    swears = ["darn", "heck", "blast", "shoot"]
    swears = list(map(prep_regexp_array, swears))
    swears = '|'.join(swears)
    return re.sub(swears, stars, string, flags=re.IGNORECASE)
    

# https://darkcoding.net/credit-card-numbers/
# https://darkcoding.net/credit-card/cvv-numbers/
def validate_card(cardnumber):
    cardnumber = re.sub(r'\D|\s', '', cardnumber)  # strip any non-digits
    cardlength = len(cardnumber)
    parity = cardlength % 2
    sum = 0
    for i in range(cardlength):
        digit = int(cardnumber[i])
        if i % 2 == parity:
            digit = digit * 2
        if digit > 9:
            digit = digit - 9
        sum = sum + digit
    valid = (sum % 10 == 0)
    return valid


# https://darkcoding.net/credit-card/luhn-formula/
def check_cc(cc, extra_check=False):
    cards = {
        "visa": "(4\d{12}(?:\d{3})?)",
        "amex": "(3[47]\d{13})",
        "jcb": "(35[2-8][89]\d\d\d{10})",
        "maestro": "((?:5020|5038|6304|6579|6761)\d{12}(?:\d\d)?)",
        "solo": "((?:6334|6767)\d{12}(?:\d\d)?\d?)",
        "mastercard": "(5[1-5]\d{14})",
        "switch": "(?:(?:(?:4903|4905|4911|4936|6333|6759)\d{12})|(?:(?:564182|633110)\d{10})(\d\d)?\d?)",
    }
    names = ["Visa", "American Express", "JCB", "Maestro", "Solo", "Mastercard", "Switch"]
    matches = []
    pattern = "#^(?:" + "|".join(cards.values()) + ")$#"
    result = re.match(pattern, cc.replace(" ", ""))
    if extra_check and result:
        result = validate_card(cc)
    return names[len(matches)-2] if result else False


def validate_uk_bank_sort_code(sort_code):
    # Remove any non-digit characters
    sort_code = re.sub(r'\D', '', sort_code)

    # Check that the length is 6 digits
    if len(sort_code) != 6:
        return False

    # Check that the first two digits are within the valid range
    first_two_digits = int(sort_code[:2])
    if not (0 <= first_two_digits <= 99):
        return False

    # Check that the third digit is within the valid range
    third_digit = int(sort_code[2])
    if not (0 <= third_digit <= 6):
        return False

    # Check that the fourth and fifth digits are within the valid range
    fourth_and_fifth_digits = int(sort_code[3:5])
    if not (0 <= fourth_and_fifth_digits <= 99):
        return False

    # Check that the sixth digit is within the valid range
    sixth_digit = int(sort_code[5])
    if not (0 <= sixth_digit <= 9):
        return False

    # All checks passed
    return True


def is_valid_uk_bank_account_number(account_number):
    account_number = account_number.replace(' ', '') # remove any spaces
    if len(account_number) != 8:
        return False
    if not account_number.isdigit():
        return False

    # Perform the algorithm for modulus check
    weights = [8, 7, 6, 5, 4, 3, 2, 1]
    total = sum(int(account_number[i]) * weights[i] for i in range(8))
    remainder = total % 11

    # If remainder is 0, account number is valid
    if remainder == 0:
        return True

    # If remainder is 1, account number is valid only if the second check passes
    if remainder == 1:
        # Perform the second check
        weights = [0, 1, 3, 1, 7, 3, 1, 7, 3]
        total = sum(int(account_number[i]) * weights[i] for i in range(9))
        remainder = total % 10
        return remainder == 0

    # If remainder is greater than 1, account number is not valid
    return False


def overly_complex_email_check(email):
    pattern = r'''
        (?:\r\n)?[ \t]*
        (?:
            (?:
                (?:
                    [^()<>@,;:\\".\[\] \x00-\x1f]+
                    (?:
                        (?:(?:\r\n)?[ \t])+ |
                        \Z |
                        (?=[\["()<>@,;:\\".\[\]])
                    )
                ) |
                "(?:[^\"\r\\]|\\.)*"
                (?:(?:(?:\r\n)?[ \t])*)+
            )
            (?:
                \.
                (?:(?:\r\n)?[ \t])*
                (?:
                    [^()<>@,;:\\".\[\] \x00-\x1f]+
                    (?:
                        (?:(?:\r\n)?[ \t])+ |
                        \Z |
                        (?=[\["()<>@,;:\\".\[\]])
                    )
                ) |
                "(?:[^\"\r\\]|\\.)*"
                (?:(?:(?:\r\n)?[ \t])*)*
            )
            *@
            (?:
                (?:
                    [^()<>@,;:\\".\[\] \x00-\x1f]+
                    (?:
                        (?:(?:\r\n)?[ \t])+ |
                        \Z |
                        (?=[\["()<>@,;:\\".\[\]])
                    )
                ) |
                \[ (?: [^\[\]\r\\] | \\. )* \]
            )
            (?:
                \.
                (?:(?:\r\n)?[ \t])*
                (?:
                    [^()<>@,;:\\".\[\] \x00-\x1f]+
                    (?:
                        (?:(?:\r\n)?[ \t])+ |
                        \Z |
                        (?=[\["()<>@,;:\\".\[\]])
                    )
                ) |
                \[ (?: [^\[\]\r\\] | \\. )* \]
            )
        )
    '''

email = "example@example.com"
if overly_complex_email_check(email):
    print("Valid email")
else:
    print("Invalid email")
