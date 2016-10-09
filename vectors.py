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

import doctest
import keyword
import math
import pdb
import unittest

DEBUG_MODE = False
if DEBUG_MODE:
    pdb.set_trace()

RESERVED = ['False', 'None', 'True', 'and', 'as', 'assert', 'break',
            'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec',
            'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
            'lambda', 'nonlocal', 'not', 'or', 'pass', 'print',
            'raise', 'return', 'try', 'while', 'with', 'yield']
KEYWORDS = keyword.kwlist

import maths, matrices


class Vector():
    legal = True
    status = r"Empty"
    dimensions = tuple()
    elements = float()
    rows = 0

    def __init__(self, vector: object) -> object:
        if type(vector) == matrices.Matrix:
            self.content = matrices.Matrix(vector).content
        elif type(vector) == Vector:
            self.content = vector.content
        else:
            self.content = vector
        # self.validate()
        self.update()

    def __str__(self):
        formatted = r""
        for row in self.content:
            formatted += str(row) + "\n"
        return formatted[:-1]

    def __eq__(self, other):
        if type(self) == Vector and type(other) == Vector:
            return self.content == other.content
        else:
            return False

    def __del__(self):
        return ()

    def measure(self):
        """
        Returns the rows of a vector revealing invalid columns
        """
        if self.content == [] or self.content == [[]]:
            return 0, 0
        else:
            rows = len(self.content)
            columns = 1
            return rows, columns

    def verify(self):
        """
        >>> print(Vector([[1],[2.0],[3j]]).verify())
        True
        
        >>> print(Vector([[1],[2],['0']]).verify())
        False
        
        >>> print(Vector([[1],[2,3],[4,5,6]]).verify())
        False
        """
        onlyone = list({len(elements) for elements in self.content})
        if not (len(onlyone) == 1 and onlyone[0] == 1):
            return False
        if ((self.rows >= 1)
            and
                (False not in [type(element) in [int, float, complex]
                               for row in self.content
                               for element in row])
            and
                (False not in [len(self.content[row]) ==
                                   len(self.content[row - 1])
                               for row in range(0, self.rows)])):
            self.legal = True
        else:
            self.legal = False
        return self.legal

    def update(self):
        self.rows, self.columns = self.size = self.measure()
        self.legal = self.verify()

    def validate(self):
        correct = [[row[0]] for row in self.content]
        self.content = correct
        self.update()

    def show(self, title=""):
        if self.content is None:
            print(r"Invalid output")
        if not title == "":
            print(title, "\n")
            return
        for row in self.content:
            print(row)

    def sequence(start, stop, gap=1):
        if gap == 0.0:
            return Vector([start, stop])
        if start == stop:
            return Vector([start, stop])
        if gap < 0.0:
            start, stop = float(max(start, stop)), float(min(start, stop))
            seq = list([start])
            point = start + gap
            while not point < stop:
                seq.append(point)
                point = point + gap
        else:
            start, stop = float(min(start, stop)), float(max(start, stop))
            seq = list([start])
            point = start + gap
            while not point > stop:
                seq.append(point)
                point = point + gap
        return Vector([seq])

    def pow(self, other):
        """
        Returns a list of powers from the exponentiation of
        bases in vec and exponents in tor
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).pow(Vector([[9], [8], [7], [6], [5], [4], [3], [2], [1], [0]])).content)
        [[0], [1], [128], [729], [1024], [625], [216], [49], [8], [1]]
        """
        # return Vector([[vec[pos][0] ** tor[pos][0] ] for pos in range(min(len(vec), len(tor)))]
        return Vector([[base[0] ** exponent[0]]
                       for (base, exponent) in zip(self.content, other.content)])

    def mul(self, other):
        """
        Returns a list of products from the multiplication of
        multiplicands in vec and multipliers in tor
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).mul(Vector([[9], [8], [7], [6], [5], [4], [3], [2], [1], [0]])).content)
        [[0], [8], [14], [18], [20], [20], [18], [14], [8], [0]]
        """
        # return Vector([[vec[pos][0] * tor[pos][0] ] for pos in range(min(len(vec), len(tor)))]
        return Vector([[multiplicand[0] * multiplier[0]]
                       for (multiplicand, multiplier) in zip(self.content, other.content)])

    def add(self, other):
        """
        Returns a list of sums from the addition of
        augends in vec and addends in tor
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).add(Vector([[9], [8], [7], [6], [5], [4], [3], [2], [1], [0]])).content)
        [[9], [9], [9], [9], [9], [9], [9], [9], [9], [9]]
        """
        # [vec[pos] + tor[pos] for pos in range(min(len(vec), len(tor)))]
        return Vector([[augend[0] + addend[0]]
                       for (augend, addend) in zip(self.content, other.content)])

    def sub(self, other):
        """
        Returns a list of differences from the subtraction of
        minuends in vec and subtrahends in tor
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).sub(Vector([[9], [8], [7], [6], [5], [4], [3], [2], [1], [0]])).content)
        [[-9], [-7], [-5], [-3], [-1], [1], [3], [5], [7], [9]]
        """
        # [vec[pos] - tor[pos] for pos in range(min(len(vec), len(tor)))]
        return Vector([[minuend[0] - subtrahend[0]]
                       for (minuend, subtrahend) in zip(self.content, other.content)])

    def div(self, other):
        """
        Returns a list of quotients from the division of
        dividends in vec and divisors in tor
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).div(Vector([[9], [8], [7], [6], [5], [4], [3], [2], [1], [0]])).content)
        [[0.0], [0.125], [0.2857142857142857], [0.5], [0.8], [1.25], [2.0], [3.5], [8.0], [inf]]
        """
        # [vec[pos] / tor[pos] for pos in range(min(len(vec), len(tor)))]
        return Vector([[dividend[0] / divisor[0]]
                       if not divisor[0] == 0 else [float("inf")]
                       for (dividend, divisor) in zip(self.content, other.content)])

    def sqrt(self):
        """
        Returns a list of square roots from the number in vector
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).sqrt().content)
        [[0.0], [1.0], [1.414213562373095], [1.7320508075688772], [2.0], [2.23606797749979], [2.449489742783178], [2.6457513110645907], [2.82842712474619], [3.0]]
        """
        # maths.sqrt([vector[pos]) for pos in range(len(self))]
        return Vector([[maths.sqrt(maths.absolute(root[0]))]
                       for root in self.content])

    def log(self):
        """
        Returns a list of logarithm from the number in vector
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).log().content)
        [[nan], [0.0], [0.6931471805599453], [1.0986122886681098], [1.3862943611198906], [1.6094379124341003], [1.791759469228055], [1.9459101490553132], [2.0794415416798357], [2.1972245773362196]]
        """
        # math.log([vector[pos]) for pos in range(len(self)) if not vector[pos][0] == 0]
        return Vector([[math.log(maths.absolute(loga[0]))]
                       if not loga[0] == 0 else [float("NaN")]
                       for loga in self.content])

    def exponent(self):
        """
        Returns a list of e raised to the power of the number in vector
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).exponent().content)
        [[1.0], [2.7182818284590455], [7.389056098930649], [20.08553692318766], [54.598150033144265], [148.41315910257657], [403.4287934927351], [1096.6331584284578], [2980.957987041728], [8103.083927575384]]
        """
        # math.exp([vector[pos]) for pos in range(len(self))]
        return Vector([[maths.exponent(expo[0])]
                       for expo in self.content])

    def absolute(self):
        """
        Returns a list of absolutes from the number in vector
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).absolute().content)
        [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
        """
        return Vector([[maths.absolute(positive[0])]
                       for positive in self.content])

    def negate(self):
        """
        Returns a list of negatives from the number in vector
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).negate().content)
        [[0], [-1], [-2], [-3], [-4], [-5], [-6], [-7], [-8], [-9]]
        """
        return Vector([[-(maths.absolute(negative[0]))]
                       for negative in self.content])

    def inverse(self):
        """
        Returns a list of inverse square roots from the number in vector
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).inverse().content)
        [[inf], [1.0], [0.7071067811865476], [0.5773502691896258], [0.5], [0.4472135954999579], [0.4082482904638631], [0.3779644730092272], [0.3535533905932738], [0.3333333333333333]]
        """
        return Vector([[maths.inv_sqrt(maths.absolute(inverse[0]))]
                       if not inverse[0] == 0 else [float("inf")]
                       for inverse in self.content])

    def dot(self, other):
        """
        Return the dot product from the sum of the multiplications of
        multiplicands in vec and multipliers in tor
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).dot(Vector([[9], [8], [7], [6], [5], [4], [3], [2], [1], [0]])))
        120
        """
        # return sum([vec[pos] * tor[pos] for pos in range(min(len(vec), len(tor)))]
        return sum([multiplicand[0] * multiplier[0]
                    for (multiplicand, multiplier) in zip(self.content, other.content)])

    def maximum(self, other):
        """
        Returns a list of differences from the subtraction of
        minuends in vec and subtrahends in tor
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).maximum(Vector([[9], [8], [7], [6], [5], [4], [3], [2], [1], [0]])).content)
        [[9], [8], [7], [6], [5], [5], [6], [7], [8], [9]]
        """
        # max([vec[pos], tor[pos]) for pos in range(min(len(vec), len(tor)))]
        return Vector([max(diffe, rence)
                       for (diffe, rence) in zip(self.content, other.content)])

    def minimum(self, other):
        """
        Returns a list of differences from the subtraction of
        minuends in vec and subtrahends in tor
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).minimum(Vector([[9], [8], [7], [6], [5], [4], [3], [2], [1], [0]])).content)
        [[0], [1], [2], [3], [4], [4], [3], [2], [1], [0]]
        """
        # min([vec[pos], tor[pos]) for pos in range(min(len(vec), len(tor)))]
        return Vector([min(diffe, rence)
                       for (diffe, rence) in zip(self.content, other.content)])

    def morethan(self, other):
        """
        Returns a list of differences from the subtraction of
        minuends in vec and subtrahends in tor
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).morethan(Vector([[9], [8], [7], [6], [5], [4], [3], [2], [1], [0]])))
        [False, False, False, False, False, True, True, True, True, True]
        """
        # max([vec[pos], tor[pos]) for pos in range(min(len(vec), len(tor)))]
        return [diffe > rence
                for (diffe, rence) in zip(self.content, other.content)]

    def lessthan(self, other):
        """
        Returns a list of differences from the subtraction of
        minuends in vec and subtrahends in tor
        >>> print(Vector([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]).lessthan(Vector([[9], [8], [7], [6], [5], [4], [3], [2], [1], [0]])))
        [True, True, True, True, True, False, False, False, False, False]
        """
        # min([vec[pos], tor[pos]) for pos in range(min(len(vec), len(tor)))]
        return [diffe < rence
                for (diffe, rence) in zip(self.content, other.content)]


if __name__ == '__main__':
    doctest.testmod()
    unittest.main(exit=False)
