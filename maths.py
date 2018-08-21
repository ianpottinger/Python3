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

import this
#import antigravity
import cmath
import doctest
import keyword
import math
import random
import re
import string
import time
import traceback
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

from decimal import Decimal, getcontext
from itertools import count

POINT_ONE = 0.1000000000000000055511151231257827021181583404541015625
POINT_TWO = 0.200000000000000011102230246251565404236316680908203125
POINT_THREE = 0.3000000000000000444089209850062616169452667236328125
GLOBAL_SQRT2 = 1.4142135623730950488016887242096980785696
GOLDEN_RATIO = 1.618033988749894848204586834
GLOBAL_E = 2.71828182845904523536028747135266249775724709369995
GLOBAL_PI = 3.1415926535897932384626433832795028841971
GLOBAL_PIE = 8.539734222673566
GLOBAL_TAU = GLOBAL_PI * 2
GLOBAL_LOG2E = 1.44269504088896340736
GLOBAL_LOG10E = 0.434294481903251827651
GLOBAL_LN2 = 0.693147180559945309417
GLOBAL_LN10 = 2.30258509299404568402
GLOBAL_PI_2 = 1.57079632679489661923
GLOBAL_PI_4 = 0.785398163397448309616
GLOBAL_1_PI = 0.318309886183790671538
GLOBAL_2_PI = 0.636619772367581343076
GLOBAL_2_SQRTPI = 1.12837916709551257390
GLOBAL_SQRT1_2 = 0.707106781186547524401
GLOBAL_GOOGOL = 10 ** 100
PYTHON_PI = 245850922 / 78256779
PLUS_ONE = math.log(GLOBAL_E)
MINUS_ONE = math.cos(GLOBAL_PI)
PLUS_ZERO = 0.0
MINUS_ZERO = -0.0
PLUS_INFINITY = float("inf")
MINUS_INFINITY = float("-inf")
NOT_A_NUMBER = float("NaN")
SMALL_PAN_DIGITAL = 1023456789
PAN_DIGITAL = 3816547290
LARGE_PAN_DIGITAL = 9814072356
SQRT_PAN_DIGITAL = 99066
LIGHT_SPEED = 299792458
SOUND_SPEED = 340.29
WATER_BOILING = 99.974
WATER_FREEZING = -0.0001
ABSOLUTE_ZERO = 273.15
LTUAE = 42
NINE9S = 99.9999999
NUMBERS = [int, float, complex]

kilo = 1000
mega = 1000 ** 2
giga = 1000 ** 3
tera = 1000 ** 4
peta = 1000 ** 5
exa = 1000 ** 6
zetta = 1000 ** 7
yotta = 1000 ** 8
bronto = 1000 ** 9

kibi = 1024
mebi = 1024 ** 2
gibi = 1024 ** 3
tebi = 1024 ** 4
pebi = 1024 ** 5
exbi = 1024 ** 6
zebi = 1024 ** 7
yobi = 1024 ** 8
brobi = 1024 ** 9

bits = lambda bites: bites * 8
kbps = lambda rate: rate * cycle_power(10, 3)
Mbps = lambda rate: rate * cycle_power(10, 6)
Gbps = lambda rate: rate * cycle_power(10, 9)
Tbps = lambda rate: rate * cycle_power(10, 12)
Pbps = lambda rate: rate * cycle_power(10, 15)
Ebps = lambda rate: rate * cycle_power(10, 18)
Zbps = lambda rate: rate * cycle_power(10, 21)
Ybps = lambda rate: rate * cycle_power(10, 24)
Bbps = lambda rate: rate * cycle_power(10, 27)
kB = lambda size: size * cycle_power(2, 10)
MB = lambda size: size * cycle_power(2, 20)
GB = lambda size: size * cycle_power(2, 30)
TB = lambda size: size * cycle_power(2, 40)
PB = lambda size: size * cycle_power(2, 50)
EB = lambda size: size * cycle_power(2, 60)
ZB = lambda size: size * cycle_power(2, 70)
YB = lambda size: size * cycle_power(2, 80)
BB = lambda size: size * cycle_power(2, 90)

"""
100 - (100 * (kilo / kibi) ) =              2.34375
100 - (100 * (mega / mebi) ) =              4.632568359375
100 - (100 * (giga / gibi) ) =              6.867742538452148
100 - (100 * (tera / tebi) ) =              9.050529822707176
100 - (100 * (peta / pebi) ) =              11.182158029987477
100 - (100 * (exa / exbi) ) =               13.263826201159645
100 - (100 * (zetta / zebi) ) =             15.296705274569973
100 - (100 * (yotta / yobi) ) =             17.28193874469723
100 - (100 * (1000 ** 9 / 1024 ** 9) ) =    19.220643305368384
100 - (100 * (1000 ** 10 / 1024 ** 10) ) =  21.113909477898815
"""

"""
100 - (100 * (kilo / kibi) ) =              2.34375
100 - (100 * (mega / mebi) ) =              4.632568359375
100 - (100 * (giga / gibi) ) =              6.867742538452148
100 - (100 * (tera / tebi) ) =              9.050529822707176
100 - (100 * (peta / pebi) ) =              11.182158029987477
100 - (100 * (exa / exbi) ) =               13.263826201159645
100 - (100 * (zetta / zebi) ) =             15.296705274569973
100 - (100 * (yotta / yobi) ) =             17.28193874469723
100 - (100 * (1000 ** 9 / 1024 ** 9) ) =    19.220643305368384
100 - (100 * (1000 ** 10 / 1024 ** 10) ) =  21.113909477898815
"""

# GLOBAL_PI = 22/7		# Assigning PI using a float division expression
POINT_ONE + POINT_TWO == POINT_THREE

##if not GLOBAL_PI == math.pi:
##    GLOBAL_PI = math.pi
##
##if not GLOBAL_E == math.e:
##    GLOBAL_E = math.e

first = 245850922  # Integer
second = 78256779.0  # Floating point
third = 11j  # Complex

# Numerical operator order of precedence.
# Exponentiation
Power = lambda base, exponent: cycle_power(base, exponent)
# Multiplication
Multiply = lambda multiplicands, multiplier: multiplicands * multiplier
# Division
Divide = lambda dividend, divisor: dividend / divisor
Division = lambda numerator, denominator: numerator / denominator
# Rounded down
Roundown = lambda dividend, divisor: dividend // divisor
# Remainder modulo
Remainder = lambda dividend, divisor: remainder(dividend, divisor)
# Addition
Add = lambda augend, addend: augend + addend
# Subtraction
Subtract = lambda minuend, subtrahend: minuend - subtrahend
# Group
Group = {'Add': Add, 'Subtract': Subtract}
# Ring
Ring = {'Add': Add, 'Subtract': Subtract, 'Multiply': Multiply}
# Field
Field = {'Add': Add, 'Subtract': Subtract, 'Multiply': Multiply, 'Division': Division}
# Less than
Less = lambda term, compare: term < compare
# More than
More = lambda term, compare: term > compare
# Equal to
Equal = lambda term, compare: term == compare
# Bitwise Left-shift
Lshift = lambda value, places: value << places
# Bitwise Right-shift
Rshift = lambda value, places: value >> places
# Bitwise NOT
NOT = lambda term, compare: term != compare
# Bitwise AND
AND = lambda binary, pattern: binary & pattern
# Bitwise OR
OR = lambda binary, pattern: binary | pattern
# Bitwise complement
Com = lambda value: ~ value
# Bitwise XOR
XOR = lambda term, compare: term ^ compare

operators = {'**': Power, '*': Multiply,
             '/': Divide, '÷': Division, '//': Roundown, '%': Remainder,
             '+': Add, '-': Subtract,
             '<': Less, '>': More, '=': Equal,
             '<<': Lshift, '>>': Rshift,
             '!=': NOT, '&': AND, '|': OR, '~': Com, '^': XOR}

# Logical operator order of precedence. NOT AND OR
var = not first > second and first == third * 2 or second != third
'Returns True' == 'Returns True'
'Returns True' != 'Returns False'
'Turns' in "Returns"
'TURNS' in 'Returns'
'turns' in "Returns"
'lowercase' > 'UPPERCASE'
'do' in "don't"


def memoise(function):
    cache = {}

    def memoised(*args):
        if args not in cache:
            cache[args] = function(*args)
        return cache[args]

    return memoised


def love(mistake):
    try:
        int(mistake) / 0
    except:
        mistake = "Undefined"
    return mistake


def is_number(number):
    try:
        type(number) in NUMBERS
        return True
    except ValueError:
        traceback.print_tb(ValueError.__traceback__)
        return False
    except SyntaxError:
        traceback.print_tb(SyntaxError.__traceback__)
        return False
    except NameError:
        traceback.print_tb(NameError.__traceback__)
        return False


def same(number):
    return sqrt(cycle_power(number, 2) + (number * 6) + 9)


def remainder(dividend, divisor):
    """
    Returns the remainder of a dividend from the divisor without using modulus
    """
    return dividend - ((dividend // divisor) * divisor)
lam_remainder = lambda dividend, divisor : dividend - ((dividend // divisor) * divisor)


def div_mod(dividend, divisor):
    """
    Returns the floor division of the dividend by the divisor and the remainder
    """
    return dividend // divisor, remainder(dividend, divisor)
lam_div_mod = lambda dividend, divisor : (dividend // divisor, remainder(dividend, divisor))


def whole_division(numerator, denominator):
    """
    >>> numerator, denominator = first, second
    >>> quotient, remainder = whole_division (numerator, denominator)
    >>> print (numerator, "/", denominator, "is", quotient, "remainder", remainder)
    245850922 / 78256779.0 is 3 remainder 11080585
    """
    return int(numerator // denominator), int(numerator % denominator)
lam_whole_division = lambda numerator, denominator : (int(numerator // denominator), int(numerator % denominator))


def absolute(number: NUMBERS) -> NUMBERS:
    """
    Returns the absolute positive of a number
    """
    return number if number > 0 else -number
lam_absolute = lambda number : number if number > 0 else -number


def opposite(number: NUMBERS) -> NUMBERS:
    """
    Returns the absolute positive of a number
    """
    return -number if number > 0 else -number
lam_opposite = lambda number : -number if number > 0 else -number


def roundup(number):
    #return math.ceil(number)
    return (number // 1) + 1


def roundown(number):
    #return math.floor(number)
    return (number // 1)


##def fract(mantissa, exponent):
##    return mantissa * exp(2, exponent)

def mean(LofN):
    """
    Returns the average mean from a list of numbers by dividing the sum of the
    numbers with the number of numbers in the list
    """
    print(LofN)
    size = len(LofN)
    if size == 0:
        # If list is empty, return zero
        return 0
    if size == 1:
        # If only a single number is in the list, return it
        return LofN[0]
    return sum(LofN) / size


def median(LofN):
    """
    Returns the average median from a list of numbers by sorting the numbers into
    order and finding the number closet to the centre of the list
    """
    size = len(LofN)
    if size == 0:
        # If list is empty, return zero
        return 0
    if size == 1:
        # If only a single number is in the list, return it
        return LofN[0]
    half = size // 2
    LofN.sort()
    if size % 2 == 1:
        # Return the centre number
        return LofN[half]
    else:
        # Return the mean of the centre numbers
        return (LofN[half - 1] + LofN[half]) / 2


def mode(LofN):
    """
    Returns the average mode from a list of numbers by dividing the sum of the
    numbers with the number of unique numbers in the list
    """
    size = len(LofN)
    if size == 0:
        """If list is empty, return zero"""
        return 0
    if size == 1:
        """If only a single number is in the list, return it"""
        return LofN[0]
    return sum(LofN) / len(set(LofN))


def scale(value, minimum, maximum, average):
    return (value - average) / (maximum - minimum)


def find_scale(value, LofN):
    minimum = min(LofN)
    maximum = max(LofN)
    average = mean(LofN)
    return scale(value, minimum, maximum, average)


def cycle_power(base, exponent):
    """
    Returns the power of the base with the exponent recursively
    """
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if exponent < 0:
        return base - exponent
    product = base * base
    # print (product)
    answer = cycle_power(product, exponent // 2)
    if exponent % 2 == 1:
        return base * answer
    else:
        return answer


def expo(base):
    """7427466391"""
    return GLOBAL_E ** base


def square(base):
    return base * base


def squared(base):
    return cycle_power(base, 2)


def cube(base):
    return base * base * base


def cubed(base):
    return cycle_power(base, 3)


def square_radius(radius):
    """(radius) -> radius squared"""
    return absolute(cycle_power(radius, 2))


def cube_radius(radius):
    """(radius) -> radius cubed"""
    return absolute(cycle_power(radius, 3))


def circle_area(radius):
    """(radius of circle) -> area of circle"""
    return square_radius(radius) * GLOBAL_PI


def circumference(radius):
    """(radius of circle) -> circumference of circle"""
    return absolute(radius) * GLOBAL_TAU


def sphere_area(radius):
    """(radius of sphere) -> area of sphere"""
    return square_radius(radius) * 4 * GLOBAL_PI


def sphere_volume(radius):
    """(radius of sphere) -> volume of sphere"""
    return cube_radius(radius) * GLOBAL_PI * (4 / 3)


def square_area(height, width):
    return absolute(height) * absolute(width)


def triangle_hypotenuse(base, height):
    return sqrt(square_radius(base) + square_radius(height))


def is_triangle(first, second, third):
    max_side = max(first, second, third)

    if max_side == first:
        return (second + third) > first
    elif max_side == second:
        return (first + third) > second
    else:
        return (first + second) > third


def triangle_perimeter(first, second, third):
    """(number, number, number) -> number
    Returns the primeter of a triangle from the lengths of the sides"""
    return absolute(first) + absolute(second) + absolute(third)


def triangle_area(base, height):
    """(number, number) -> number
    Returns the area of a triangle from the base and height"""
    return square_area(base, height) / 2


def triangle_heron(first, second, third):
    """(number, number, number) -> number
    Returns the area of a triangle, given the lengths of its three sides."""

    # Use Heron's formula
    halfsides = triangle_perimeter(first, second, third) / 2
    return sqrt(halfsides *
                (halfsides - first) *
                (halfsides - second) *
                (halfsides - third))


def hexagon_area(radius):
    return square_radius(radius) * 3 * (sqrt(3) / 2)


def polygon_area(sides, length):
    return (1 / 4) * sides * cycle_power(length, 2) / math.tan(GLOBAL_PI / sides)


def surface_area(height, width, depth):
    height = absolute(height)
    width = absolute(width)
    depth = absolute(depth)
    if height == width == depth:
        return 6 * (width ** 2)
    else:
        return ((2 * (height * width)) +
                (2 * (width * depth)) +
                (2 * (depth * height)))


def cube_volume(height, width, depth):
    height = absolute(height)
    width = absolute(width)
    depth = absolute(depth)
    if height == width == depth:
        return cube_radius(width)
    else:
        return height * width * depth


ratio_percent = lambda ratio, total: (ratio * 100) / total
fraction_percent = lambda numerator, denominator: (numerator / denominator) * 100
decimal_percent = lambda decimal: decimal * 100
percent_percent = lambda per, cent: ((per / 100) * (cent / 100)) * 100
percent_diff = lambda initial, current: ((current - initial) / initial) * 100


def sqrt(number, progress = False):
    """
    >>> sqrt(100)
    10.0
    >>> sqrt(81)
    9.0
    >>> sqrt(64)
    8.0
    >>> sqrt(49)
    7.0
    >>> sqrt(36)
    6.0
    >>> sqrt(25)
    5.0
    >>> sqrt(16)
    4.0
    >>> sqrt(9)
    3.0
    >>> sqrt(4)
    2.0
    >>> sqrt(2)
    1.414213562373095
    >>> sqrt(1)
    1.0
    >>> sqrt(0)
    0.0
    >>> inv_sqrt(9)
    0.3333333333333333
    """
    if number == 0:
        return 0.0
    if number == 1:
        return 1.0
    number = absolute(number)

    guess = cycle_power(2, (math.log(number, 2) / 2))  # best initial square root guess
    attempts = 1
    workings = [guess]

    previous = 0
    while guess != previous:
        previous = guess
        # print (guess)
        guess = 0.5 * (guess + number / guess)
        attempts += 1
        workings += [guess]

    if progress:
        return guess, attempts, workings
    else:
        return guess


inv_sqrt = lambda number: 1 / sqrt(number)


def approx_eq(num, ber, tolerance = 1e-12):
    return absolute(num - ber) <= tolerance


def square_root(number):
    """Compute the square root of x by mutually recursive Newton's method.

    1.414213562373095 0488016887242096980785696

    >>> square_root(100)
    10.0
    >>> square_root(81)
    9.0
    >>> square_root(64)
    8.0
    >>> square_root(49)
    7.0
    >>> square_root(36)
    6.0
    >>> square_root(25)
    5.0
    >>> square_root(16)
    4.000000000000051
    >>> square_root(9)
    3.0
    >>> square_root(2)
    1.414213562373095
    """

    number = absolute(number)

    def guess_sqrt(guess):
        if approx_eq(guess * guess, number):
            return guess
        # print (guess)
        return guess_again(guess)

    def guess_again(guess):
        return guess_sqrt(0.5 * (guess + number / guess))

    guess = cycle_power(2, (math.log(number, 2) / 2))  # best initial square root guess
    return float(guess_sqrt(cycle_power(2, guess)))


inverse_square_root = lambda number: 1 / square_root(number)


def guess_attempts(low, high):
    """
    >>> guess_attempts(0, 1000)
    10
    >>> guess_attempts(500, 1000)
    9
    >>> guess_attempts(350, 550)
    8
    """
    return math.ceil(math.log((max(high, low)) - (min(low, high)) + 1, 2))


def range_divisors(number, start, finish):
    """ (int) -> lst

    Return list of integers between the start and finish range
    that number can be divided by.

    >>> range_divisors (-10, 6, -6)
    [5, 2, 1, -1, -2, -5]
    """
    collector = []
    if number == 0:
        return collector
    for divisor in range(max(start, finish), min(start, finish), -1):
        if divisor != 0:
            if number % divisor == 0:
                collector += [divisor]
    return collector


def all_divisors(number):
    """
    >>> all_divisors(60)
    [30, 20, 15, 12, 10, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -10, -12, -15, -20, -30]
    >>> all_divisors(120)
    [60, 40, 30, 24, 20, 15, 12, 10, 8, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -8, -10, -12, -15, -20, -24, -30, -40, -60]
    >>> all_divisors(180)
    [90, 60, 45, 36, 30, 20, 18, 15, 12, 10, 9, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -9, -10, -12, -15, -18, -20, -30, -36, -45, -60, -90]
    >>> all_divisors(240)
    [120, 80, 60, 48, 40, 30, 24, 20, 16, 15, 12, 10, 8, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -8, -10, -12, -15, -16, -20, -24, -30, -40, -48, -60, -80, -120]
    >>> all_divisors(100)
    [50, 25, 20, 10, 5, 4, 2, 1, -1, -2, -4, -5, -10, -20, -25, -50]
    """
    half = number // 2
    return range_divisors(number, half, -half - 1)


extract_digits = lambda x: "".join(char for char in x if char in string.digits + ".")
to_float = lambda x: float(x) if x.count(".") <= 1 else None


# Kinematic Equations

def speed(distance, time):
    return distance / time


def velocity(displacement, time):
    return displacement / time


def acceleration():
    return velocity / time


def displacement(time, initial=None, final=None, acceleration=None):
    values = [initial, final, acceleration]
    nuns = values.count(None)

    if nuns > 1:
        return None
    elif acceleration == None:
        return .5 * (final + initial) * time
    elif final == None:
        return initial * time + .5 * acceleration * time ** 2
    elif initial == None:
        return final * time - .5 * acceleration * time ** 2
    else:
        return .5 * (initial + final) / acceleration


def final_velocity(initial, acceleration, time):
    return initial + acceleration * time


def final_velocity_squared(initial, acceleration, displacement):
    return initial ** 2 + 2 * acceleration * displacement


def rabin_miller(number):
    # Returns True if number is a prime number.

    s = number - 1
    t = 0
    while s % 2 == 0:
        # keep halving s until it is even (and use t
        # to count how many times we halve s)
        s //= 2
        t += 1

    for trials in range(5):  # try to falsify number's primality 5 times
        a = random.randrange(2, number - 1)
        v = pow(a, s, number)
        if v != 1:  # this test does not apply if v is 1.
            i = 0
            while v != (number - 1):
                if i == t - 1:
                    return False
                else:
                    i += 1
                    v = (v ** 2) % number
    return True


def naive_prime(number):
    from itertools import count, islice
    primes = (number for number in count(2)
              if all(number % d for d in range(2, number)))
    return islice(primes, 0, number)


def regex_prime(number):
    # see http://www.noulakaz.net/weblog/2007/03/18/a-regular-expression-to-check-for-prime-numbers/
    return re.match(r'^1?$|^(11+?)\1+$', '1' * number) is None


def is_prime(number):
    low_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                  449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                  587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                  853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                  991, 997]
    # if number in low_primes:
    #    return True

    number *= 1.0
    for prime in low_primes:
        if number % prime == 0 and number != prime:
            return False

    for b in range(1, int((number ** 0.5 + 1) / 6.0 + 1)):
        if number % (6 * b - 1) == 0:
            return False
        if number % (6 * b + 1) == 0:
            return False
    return regex_prime(int(number))


def mersenne_prime(number: int) -> bool:  # messed up
    mersenne = cycle_power(2, number) - 1
    answer = True
    for divisor in range(2, int(sqrt(mersenne))):
        if remainder(mersenne, divisor) == 0:
            answer = True
        else:
            return False
    return answer


def lucas_lehmer(number: int) -> bool:
    if mersenne_prime(number):
        if number == 2:
            return True
        mersenne = cycle_power(2, number) - 1
        answer = 4
        for divisor in range(number - 2):
            answer = pow(answer, 2, mersenne) - 2
            # Performing the mod Mp at each iteration ensures
            # that all intermediate results are at most p bits
            # (otherwise the number of bits would double each iteration).
            # The same strategy is used in modular exponentiation.
        return answer == 0


def return_primes(number):  # Max 168
    check = 2
    hits = 0
    primes = []
    while hits != number:
        if is_prime(check):
            primes.append(check)
            hits += 1
        check += 1
    return primes


def primes41(number): # Tested 10000
    return [(n ** 2 - n) + 41 for n in range(number)]


def random_prime(keysize=1024):
    # Return a random prime number of keysize bits in size.
    while True:
        number = random.randrange(2 ** (keysize - 1), 2 ** keysize)
        if is_prime(number):
            return number


def euclid_recurse(first: object, second: object) -> object:
    return second and euclid_recurse(second, first % second) or first


def euclid_gcd(first, second):
    # Return the greatest common divisor/factor
    while first != 0:
        first, second = second % first, first
    return second


def euclid_gcd_recurse(first, second):
    if second == 0:
        return euclid_gcd_recurse(second, first % second)


def inverse_log_factorial(number):
    """ Inverse Stirling's approx for log n factorial, using Newton's method """
    LogRoot2Pi = .5 * math.log(2. * math.pi)
    Log10 = math.log(10.)
    result = constant = number * Log10 - LogRoot2Pi

    for iteration in range(3):
        result = (constant + result) / math.log(result)
    return int(round(result))


def modular_inverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a * x % m = 1

    if euclid_gcd(a, m) != 1:
        return None  # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3  # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def extended_gcd(first, second):
    x, y, u, v = 0, 1, 1, 0
    while first != 0:
        q, r = second // first, second % first
        m, n = x - u * q, y - v * q
        second, first, x, y, u, v = first, r, u, v, m, n
    return second, x, y


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


def recursive_egcd(first, second):
    if first == 0:
        return second, 0, 1
    else:
        g, y, x = recursive_egcd(second % first, first)
        return g, x - (second // first) * y, y


def multiplicative_inverse(first, second):
    original_first = first
    X = 0
    previous_X = 1
    Y = 1
    previous_Y = 0
    while second != 0:
        temp = second
        quotient = first / second
        second = first % second
        first = temp
        temp = X
        first = previous_X - quotient * X
        previous_X = temp
        temp = Y
        Y = previous_Y - quotient * Y
        previous_Y = temp

    return original_first + previous_Y


def balance(value):
    if value > 0:
        print(r"positive")
    elif value < 0:
        print(r"negative")
    else:
        print(r"eventive")
    # print (1 if value > 0 else -1 if value < 0 else 0)
    return 1 if value > 0 else -1 if value < 0 else 0


def is_leap_year(year):
    """ (int) -> bool

    >>> is_leap_year (2000)
    True
    >>> is_leap_year (2002)
    False
    >>> is_leap_year (2020)
    True
    >>> is_leap_year (2022)
    False
    """

    def test_is_leap_year(self):
        actual = is_leap_year(2000)
        expected = True
        self.assertEqual(actual, expected)

        actual = is_leap_year(2002)
        expected = False
        self.assertEqual(actual, expected)

        actual = is_leap_year(2020)
        expected = True
        self.assertEqual(actual, expected)

        actual = is_leap_year(2022)
        expected = False
        self.assertEqual(actual, expected)

    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False


@memoise
def return_change(amount,
                  kinds=(5000, 2000, 1000, 500, 100, 50, 10, 5, 1)):
    if amount == 0:
        return 1
    if len(kinds) == 0:
        return 0
    if amount < 0:
        return 0
    d = kinds[0]
    # print (locals() )
    return return_change(amount, kinds[1:]) + return_change(amount - d, kinds)


def find_number_with_or_without_decimal(mystring):
    return re.findall(r"^\.?\d+", mystring)


smaller_of_largest = lambda L1, L2: min(max(L1), max(L2))
larger_of_smallest = lambda L1, L2: max(min(L1), min(L2))


def factorial_iter(number):
    total, k = 1, 1
    while k <= number:
        total, k = total * k, k + 1
    return total


expotenial = lambda number: sum(1.0 / factorial_iter(step) for step in range(number))

factorial = lambda number: number * factorial(number - 1) if not number == 1 else 1


@memoise
def factorial_cache(number):
    if number == 1:
        return 1
    return number * factorial_cache(number - 1)


def fibonacci_iter(number):
    previous, current = 1, 0
    if number == 1:
        return 0
    if number == 2:
        return 1
    for step in range(number - 1):
        previous, current = current, previous + current
    return current


def fibonacci_gen(number):
    previous, current = 1, 0
    if number == 1:
        return 0
    if number == 2:
        return 1
    while True:
        previous, current = current, previous + current
        yield current


@memoise
def fibonacci(number):
    if number == 1:
        return 0
    if number == 2:
        return 1
    return fibonacci(number - 2) + fibonacci(number - 1)


def round_golden_powers(iterations, last=False):
    """
    a.k.a. Lucus
    limited to 1474
    """
    if iterations > 1474:
        return -1
    elif last:
        return round(cycle_power(GOLDEN_RATIO, iterations))
    else:
        chain = []
        if not last:
            for link in range(abs(iterations)):
                chain.append(round(cycle_power(GOLDEN_RATIO, link)))
            return chain


def permutations(items, draws):
    result = 1
    for draw in range(items, items - draws, -1):
        result *= draw
    return result


def combinations(items, draws):
    return permutations(items, draws) / factorial(draws)


def mandel(z):
    c = z
    maxiter = 80
    for n in range(1, maxiter):
        if abs(z) > 2:
            return n - 1
        z = cycle_power(z, 2) + c
    return maxiter


"""convert from Julia
def randmatstat(t)
    n = 5
    v = zeros(t)
    w = zeros(t)
    for i in range(len(t) ):
        a = randn(n,n)
        b = randn(n,n)
        c = randn(n,n)
        d = randn(n,n)
        P = [a b c d]
        Q = [a b; c d]
        v[i] = trace((P.'*P)^4)
        w[i] = trace((Q.'*Q)^4)
    end
    std(v)/mean(v), std(w)/mean(w)
end
"""

##>>> return_celsius (32)
##0.0
##>>> return_celsius (212)
##100.0
return_celsius = lambda fahrenheit: (fahrenheit - 32) / 1.8

##>>> return_fahrenheit (0)
##32.0
##>>> return_fahrenheit (100)
##212.0
return_fahrenheit = lambda celsius: celsius * 1.8 + 32

##>>> return_kelvin (32)
##273.15
##>>> return_kelvin (212)
##373.15
return_kelvin = lambda fahrenheit: return_celsius(fahrenheit) + 273.15

return_psi = lambda bar: bar * 14.5037738007

return_bar = lambda psi: psi * 0.0689475728001037

return_miles = lambda km: km * 0.6213712

return_knots = lambda km: km * 0.539957


def future_value(present_value, annual_rate, periods_per_year, years):
    """
    >>> print (future_value(1000, .02, 365, 3) )
    1061.8348011259045
    >>> print (future_value(500, .04, 10, 10))
    745.3174428239327
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value * (1 + rate_per_period) ** periods


def project_to_distance(point_x, point_y, distance):
    dist_to_origin = sqrt(cycle_power(point_x, 2) +
                          cycle_power(point_y, 2))
    scale = distance / dist_to_origin
    return point_x * scale, point_y * scale


def distance_between_points(vector1, vector2):
    return sqrt((vector1[0] - vector2[0]) ** 2 +
                (vector1[1] - vector2[1]) ** 2)


def distance_on_unit_sphere(lat1, long1, lat2, long2):
    # Convert latitude and longitude to
    # spherical coordinates in radians.
    degrees_to_radians = GLOBAL_PI / 180.0

    # phi = 90 - latitude
    phi1 = (90.0 - lat1) * degrees_to_radians
    phi2 = (90.0 - lat2) * degrees_to_radians

    # theta = longitude
    theta1 = long1 * degrees_to_radians
    theta2 = long2 * degrees_to_radians

    # Compute spherical distance from spherical coordinates.

    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length

    cos = (math.sin(phi1) * math.sin(phi2) *
           math.cos(theta1 - theta2) +
           math.cos(phi1) * math.cos(phi2))
    arc = math.acos(cos)

    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    # http://www.johndcook.com/lat_long_details.html
    return arc


def find_closest_distance(coordinates):
    """
    >> coordinates = [[random.random() for long in range(10)] for lat in range(4)]
    >> find_closest_distance(coordinates)
    >> find_furthest_distance(coordinates)
    """
    if len(coordinates) < 4:
        return 0
    return min([distance_on_unit_sphere(lat1, long1, lat2, long2) \
                for lat1 in coordinates[0] for long1 in coordinates[1] \
                for lat2 in coordinates[2] for long2 in coordinates[3]])


def find_furthest_distance(coordinates):
    """
    >> coordinates = [[random.random() for long in range(10)] for lat in range(4)]
    >> find_closest_distance(coordinates)
    >> find_furthest_distance(coordinates)
    """
    if len(coordinates) < 4:
        return 0
    return max([distance_on_unit_sphere(lat1, long1, lat2, long2) \
                for lat1 in coordinates[0] for long1 in coordinates[1] \
                for lat2 in coordinates[2] for long2 in coordinates[3]])


# Counting factors

def count_factors(number):
    """Count the positive integers that evenly divide number.

    >>> count_factors(576)
    21
    """
    factors = 0
    for k in range(1, number + 1):
        if number % k == 0:
            factors += 1
    return factors


def count_factors_fast(n):
    """Count the positive integers that evenly divide n.

    >>> count_factors_fast(576)
    21
    """
    sqrt_n = sqrt(n)
    k, factors = 1, 0
    while k < sqrt_n:
        if n % k == 0:
            factors += 2
        k += 1
    if k * k == n:
        factors += 1
    return factors


# Exponentiation

def re_exp(base, exponent):
    """Returns the base to the power of the exponent.

    >>> re_exp(2, 10)
    1024
    """
    if exponent == 0:
        return 1
    return base * re_exp(base, exponent - 1)


def fast_exp(b, n):
    """Return b to the n.

    >>> fast_exp(2, 10)
    1024
    """
    if n == 0:
        return 1
    if n % 2 == 0:
        return square(fast_exp(b, n // 2))
    else:
        return b * fast_exp(b, n - 1)


def fast_fourier_transform(sequence):
    """
    >>> sample = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
    >>> print( ' '.join("%5.3f" % abs(f) for f in fast_fourier_transform(sample)) )
    4.000 2.613 0.000 1.082 0.000 1.082 0.000 2.613
    """
    elements = len(sequence)
    if elements <= 1:
        return sequence
    even = fast_fourier_transform(sequence[0::2])
    odd = fast_fourier_transform(sequence[1::2])
    return [even[k] + cmath.exp(-2j * GLOBAL_PI * k / elements) *
            odd[k] for k in range(elements // 2)] + \
           [even[k] - cmath.exp(-2j * GLOBAL_PI * k / elements) *
            odd[k] for k in range(elements // 2)]


def collatz_conjecture(start):
    start = abs(start)
    while not start == 1:
        if round(start) % 2 == 0:
            start //= 2
            print(start)
        else:
            start = start * 3 + 1
            print(start)
    return None


def sum_triangle_rows(rows, show=False):
    triangle = []
    counter = 0
    result = 0

    for row in range(rows):
        line = []
        for block in range(row):
            counter += 1
            line.append(counter)
        triangle.append(line)
        result += sum(triangle[-1])

    if show:
        for line in triangle:
            print(line)
    return result


def sum_pascal_rows(rows, show=False):
    triangle = []
    result = 0

    for row in range(rows):
        line = []
        counter = 0
        for block in range(row):
            counter += 1
            line.append(counter)
        triangle.append(line)
        result += sum(triangle[-1])

    if show:
        for line in triangle:
            print(line)
    return result


##>>> triangle_numbers(14)
##[0.0, 1.0, 3.0, 6.0, 10.0, 15.0, 21.0, 28.0, 36.0, 45.0, 55.0, 66.0, 78.0, 91.0]
triangle_numbers = lambda rows: [row * (row + 1) / 2 for row in range(rows)]
##>>> triangular(14)
##91
triangular = lambda number: sum(range(number))


def pascal_triangle(rows):
    for rownum in range(rows):
        newValue = 1
        PrintingList = [newValue]
        for iteration in range(rownum):
            newValue = newValue * (rownum - iteration) * 1 / (iteration + 1)
            PrintingList.append(int(newValue))
        print(PrintingList)
    print()


def angle_to_vector(angle):
    return [math.cos(angle), math.sin(angle)]


"""
Double every second digit, from the rightmost: (1×2) = 2, (8×2) = 16, (3×2) = 6, (2×2) = 4, (9×2) = 18
Sum all the individual digits (digits in parentheses are the products from Step 1): x (the check digit) + (2) + 7 + (1+6) + 9 + (6) + 7 + (4) + 9 + (1+8) + 7 = x + 67.
If the sum is a multiple of 10, the account number is possibly valid. Note that 3 is the only valid digit that produces a sum (70) that is a multiple of 10.
Thus these account numbers are all invalid except possibly 79927398713 which has the correct checkdigit.
"""


def luhn_checksum(card_number):
    def digits_of(number):
        return [int(digit) for digit in str(number)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for digit in even_digits:
        checksum += sum(digits_of(digit * 2))
    return checksum % 10


def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0


def calculate_luhn(partial_card_number):
    check_digit = luhn_checksum(int(partial_card_number) * 10)
    return check_digit if check_digit == 0 else 10 - check_digit


"""
Append a zero check digit to the partial number and calculate checksum
If the (sum mod 10) == 0, then the check digit is 0
Else, the check digit = 10 - (sum mod 10)
"""


def long_pi():
    """Compute Pi to the current precision.

    >>> print (long_pi() )
    3.141592653589793238462643383

    """
    getcontext().prec += 2  # extra digits for intermediate steps
    three = Decimal(3)  # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s  # unary plus applies the new precision


def exponent(x):
    """Return e raised to the power of x.  Result type matches input type.

    >>> print (exponent(Decimal(1)) )
    2.718281828459045235360287471
    >>> print (exponent(Decimal(2)) )
    7.389056098930650227230427461
    >>> print (exponent(2.0) )
    7.389056098930649
    >>> print (exponent(2+0j) )
    (7.389056098930649+0j)

    """
    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
    getcontext().prec -= 2
    return +s


def cosine(radians):
    """Return the cosine of x as measured in radians.

    >>> print (cosine(Decimal('0.5')) )
    0.8775825618903727161162815826
    >>> print (cosine(0.5) )
    0.8775825618903728
    >>> print (cosine(0.5+0j) )
    (0.8775825618903728+0j)

    """
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i - 1)
        num *= radians * radians
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s


def sine(radians):
    """Return the sine of x as measured in radians.

    >>> print (sine (Decimal('0.5')) )
    0.4794255386042030002732879352
    >>> print (sine (0.5) )
    0.479425538604203
    >>> print (sine (0.5+0j) )
    (0.479425538604203+0j)

    """
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, radians, 1, radians, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i - 1)
        num *= radians * radians
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s


def triangle_sine(n):
    #    tsin
    #        n - number
    #        returns the triangular sine of n
    x = n % 1
    if x <= .25:
        return x
    if x <= .75:
        return .5 - x
    return x - 1


def my_angle_to_vector(angle):
    return [cosine(angle), sine(angle)]


def quadratic(a, b, c):
    discriminant = sqrt(b * b - 4 * a * c)
    return (-b + discriminant) / (2 * a), (-b - discriminant) / (2 * a)


def TPC(desired, measured, current):
    """
    Signal Power Control
    >>> TPC(2.2,1.64,2)
    2.682926829268293
    """
    return (desired / measured) * current


def MSIR(current, measured, interference, noise):
    """
    Measured Signal to Interference Ratio
    >>> MSIR(.9,1.4,[.1*1.50, .2*2.68],.1)
    1.6030534351145038
    """
    return (current * measured) / (sum(interference) + noise)


def DPC(desired, measured, current):
    """
    Distributed Power Control for quality
    >>> DPC(2.2,1.64,2)
    2.682926829268293
    """
    next_power = (desired / measured) * current
    return next_power


def base_station(desired, current, measured, interference, noise):
    """
    Receiver
    """

    return DPC(desired, MSIR(current, measured, interference, noise), current)


def mobile_station(current, desired):
    """
    Transmitter
    """
    return current, desired


def endpoint_wifi_throughput(bandwidth, stations, transmit_probability=None):
    """
    Returns the likely Wi-Fi throughput out of the maximum bandwidth of
    endpoints sharing the same band connected to an access point
    >>> bandwidth = 54
    >>> stations = 5
    >>> endpoint_wifi_throughput(bandwidth, stations)
    4.423680000000001
    """
    if not transmit_probability is None:
        transmit_probability = abs(transmit_probability)
    if transmit_probability is None:
        transmit_probability = (100 / stations) / 100
    elif transmit_probability >= 1:
        transmit_probability /= 100
    endpoint_throughput = transmit_probability * ((1 - transmit_probability)
                                                  ** (stations - 1))
    return bandwidth * endpoint_throughput


def access_point_throughput(bandwidth, stations, transmit_probability=None):
    """
    Returns the likely throughput from the maximum bandwidth of an access point
    with a number of connected endpoints sharing the same band
    >>> bandwidth = 54
    >>> stations = 5
    >>> access_point_throughput(bandwidth, stations)
    22.118400000000005
    """
    return endpoint_wifi_throughput(bandwidth, stations, transmit_probability) * stations


def cwnd():
    """
    Congestion window time
    """
    return


def RTT(bandwidth_delay, nodes):
    """
    Round Trip Time
    """
    return 2 * (bandwidth_delay * nodes)


def SRTT(srtt, rtt):
    return (0.9 * srtt) + (0.1 * rtt)


def Svar(srtt, rtt, svar):
    return (0.9 * svar) + (0.1 * (rtt - srtt))


def adaptive_timeout(srtt, svar):
    return srtt + (4 * svar)


def RMSE():
    """
    Returns the Root Mean Square Error
    Take raw average
    Take square difference
    Take mean of sqaure differences
    Take square root set
    """
    return


def BEB():
    """
    Binary Exponential Backoff
    """
    return


def Statistical_Multiplexing():
    """
    Binomial probabilities 
    """

    return


def transmit_delay(bits, rate):
    """
    Time to put the message on the wire
    """
    return bits / rate


def propagate_delay(bits, speed):
    """
    Time for the bits of the message to propagate across the wire
    """
    return bits / speed


def message_latency(bits, rate, speed):
    """
    Returns the time taken to transmit a message
    """
    return speed + (transmit_delay(bits, rate) / propagate_delay(bits, speed)) * 1000


def bandwidth_delay(rate, delay):
    """
    Returns the product of the link capacity and link delay
    """
    return rate * (delay * cycle_power(10, -3))


def dB(signal, noise):
    """
    Signal to noise ratio in decibels
    """
    return 10 * math.log((signal / noise), 10)


def nyquist_limit(frequency, levels):
    """
    Given the bandwidth in Mhz and number of signal levels
    Returns the maximum kbps rate of transfer across a medium without noise
    """
    return (2 * frequency) * math.log(levels, 2)


def shannon_capacity(bandwidth, signal, noise):
    """
    Maximum reliable bitrate of data transfer across the channel
    """
    return bandwidth * math.log((1 + (signal / noise)), 2)


def channel_capacity(bandwidth, signal, noise):
    """
    Maximum reliable bitrate of data transfer across the channel
    """
    return bandwidth * math.log((1 + dB(signal, noise)), 2)


def narcissists():
    for digits in count(0):
        digitpowers = [i ** digits for i in range(10)]
        for n in range(int(10 ** (digits - 1)), 10 ** digits):
            div, digitpsum = n, 0
            while div:
                div, mod = divmod(div, 10)
                digitpsum += digitpowers[mod]
            if n == digitpsum:
                yield n


def hanoi(disks, startPeg=1, endPeg=3):
    if disks:
        hanoi(disks - 1, startPeg, 6 - startPeg - endPeg)
        print(f"Move disk {disks} from peg {startPeg} to {endPeg}")
        hanoi(disks - 1, 6 - startPeg - endPeg, endPeg)


def recursion(number):
    print(number)
    if number > 100:
        return number - 10
    else:
        return recursion(recursion(number + 11))


def deep_recursion(M, N):
    if M == 0:
        return N + 1
    elif N == 0:
        return deep_recursion(M - 1, 1)
    else:
        return deep_recursion(M - 1, deep_recursion(M, N - 1))


def show_deep_recursion(m, n, s="%s"):
    """
    show_deep_recursion(2, 6)
    """
    print(s % ("A(%d,%d)" % (m, n)))
    if m == 0:
        return n + 1
    if n == 0:
        return show_deep_recursion(m - 1, 1, s)
    n2 = show_deep_recursion(m, n - 1, s % ("A(%d,%%s)" % (m - 1)))
    return show_deep_recursion(m - 1, n2, s)


##def base10to(number, base):
##    while(number > 0):
##        binary = 0
##        pos = 1
##        binary = binary + (number % 2) * pos
##        number = number / 2
##        pos *= 10
##    return pos



def triangular_solve(rowlist, b):
    x = zero_vec(rowlist[0].D)
    for i in reversed(range(len(rowlist))):
        x[i] = (b[i] - rowlist[i] * x) / rowlist[i][i]
    return x


def triangular_solve(rowlist, label_list, b):
    x = zero_vec(set(label_list))
    for r in reversed(range(len(rowlist))):
        c = label_list[r]
        x[c] = (b[r] - x * rowlist[r]) / rowlist[r][c]
    return x


def populate_growth_rate(population, births, deaths):
    return (births - deaths) / population


if __name__ == '__main__':
    doctest.testmod()
    unittest.main(exit=False)
##    cProfile.run('print(all_divisors(10000000))')
##    hanoi(3)


"""
for i, n in enumerate(islice(narcissists(), 25), 1):
    print(n, end=' ')
    if i % 5 == 0: print() 
print()

0 1 2 3 4 
5 6 7 8 9 
153 370 371 407 1634 
8208 9474 54748 92727 93084 
548834 1741725 4210818 9800817 9926315 
"""
