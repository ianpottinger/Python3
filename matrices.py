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
import random
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

import maths, vectors


class Matrix():
    legal = True
    status = r'Empty'
    dimensions = tuple()
    elements = float()
    rows = 0
    columns = 0

    def __init__(self, matrix: object) -> object:
        if type(matrix) == tuple:
            self.content = Matrix.zero(*matrix).content
        elif type(matrix) == Matrix:
            self.content = matrix.content
        else:
            self.content = matrix
        self.update()
        self.verify()

    def __str__(self):
        formatted = r""
        for row in self.content:
            formatted += str(row) + "\n"
        return formatted[:-1]

    def __eq__(self, other):
        if type(self) == Matrix and type(other) == Matrix:
            return self.content == other.content
        else:
            return False

    def __del__(self):
        return ()

    def measure(self):
        """
        Returns the rows by columns of self.content
        """
        if self.content == [] or self.content == [[]]:
            return 0, 0
        else:
            # print(type(self), type(self.content))
            rows = len(self.content)
            if rows >= 1:
                columns = max({len(row) for row in self.content})
            else:
                columns = len(self.content[0])
            return rows, columns

    def verify(self):
        """
        >>> print(Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]]).verify())
        True
        
        >>> print(Matrix([[0, 0, 0], [1, 1], [0, 0, 0]]).verify())
        False

        >>> print(Matrix([[0, 0, 0], [1, 1, 1, 1], [0, 0, 0]]).verify())
        False
        """
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

    def show(self, title="", precision=0):
        """
        print(Matrix.fill(10, 10, 6))
        print(Matrix.zero(10, 10))
        >>> print(Matrix([[1,2],[3,4],[5,6]]).mul(Matrix([[11,12],[13,14],[15,16]])))
        (None, 'Size mismatch')
        
        >>> print(Matrix([[1,0,0],[0,1,0],[0,0,1]]).mul(Matrix([[1],[3],[2]])))
        [1]
        [3]
        [2]

        >>> print(Matrix([[1,3], [2,4], [0,5]]).mul(Matrix([[1,0,7], [2,3,6]])))
        [7, 9, 25]
        [10, 12, 38]
        [10, 15, 30]

        >>> print(Matrix([[16,34], [22,45], [80,51]]).mul(Matrix([[1,0], [2,3]])))
        [84, 102]
        [112, 135]
        [182, 153]

        >>> print(Matrix([[16,34], [22,45], [80,51]]).mul(Matrix([[12,40], [27,34]])))
        [1110, 1796]
        [1479, 2410]
        [2337, 4934]

        >>> print(Matrix([[1,2,-2], [3,0,-1]]).mul(Matrix([[5], [3], [2]])))
        [7]
        [13]

        """
        if self.content is None:
            print(r"Invalid output")
        if not title == "":
            print(title, "\n")
            return
        for row in self.content:
            print(row)

    def array(self):
        return self.content

    def line(self, row):
        if self.rows >= row:
            return Matrix([self.content[row]])
        else:
            return None

    def vector(self, column):
        """
        >>> Matrix([[0, -1, -2], [1, 0, -1], [2, 1, 0], [3, 2, 1]]).vector(1).show()
        [-1]
        [0]
        [1]
        [2]

        """
        if self.columns >= column:
            return vectors.Vector([[row[column]] for row in self.content])
        else:
            return None

    def element(self, row, column, segment=1):
        if column + segment > self.columns:
            return None
        if (self.rows >= row) and (self.columns >= column):
            return [self.content[row][column + count]
                    for count in range(0, segment)]
        else:
            return None

    def fix(self, row, column, value):
        if ((value in [int, float, complex]) and
                (not self.element(row, column) is None)):
            self.content[row][column] = value
            return True
        else:
            return False

    def get(self, row, column):
        if (self.rows >= row) and (self.columns >= column):
            return self.content[row][column]
        else:
            return None

    def transpose(self):
        """
        >>> Matrix([[9,8,7,6,5], [4,3,2,1,0], [0,1,2,3,4], [5,6,7,8,9]]).transpose().show()
        [9, 4, 0, 5]
        [8, 3, 1, 6]
        [7, 2, 2, 7]
        [6, 1, 3, 8]
        [5, 0, 4, 9]

        """
        ##        return Matrix([[row[column]
        ##                        for row in self.content]
        ##                       for column in range(self.columns) ] )
        ##
        ##        return Matrix([[column[row]
        ##                        for column in self.content]
        ##                       for row in range(self.columns) ] )

        return Matrix([list(element)
                       for element in zip(*self.content)])  # Clever method

    def inner(self, other):
        return

    def outer(self, other):
        return

    def diff(self, other):
        """
        >>> m=Matrix([[9,8,7,6,5], [4,3,2,1,0]])
        >>> n=Matrix([[0,1,2,3,4], [5,6,7,8,9]])
        >>> m.diff(n).show()
        [9, 7, 5, 3, 1]
        [1, 3, 5, 7, 9]

        """
        if type(other) in [int, float, complex]:
            other = Matrix.fill(self.rows, self.columns, other)
        if not self.size == other.size:
            return None, 'Size mismatch'
        else:
            return Matrix([[max(self.content[row][column],
                                other.content[row][column]) -
                            min(self.content[row][column],
                                other.content[row][column])
                            for column in range(self.columns)]
                           for row in range(self.rows)])

    """
    result = []
    for row in range(rows):
        result.append([])
        for column in range(columns):
            result[row].append(mat[row][column] 'function' rix[row][column])

    return Matrix([[mat[row][column] 'function' rix[row][column]
            for column in range(columns)]
            for row in range(rows)]
    """

    def pow(self, other):
        """
        >>> m=Matrix([[9,8,7,6,5], [4,3,2,1,0]])
        >>> n=Matrix([[0,1,2,3,4], [5,6,7,8,9]])
        >>> m.pow(n).show()
        [1, 8, 49, 216, 625]
        [1024, 729, 128, 1, 0]

        """
        if type(other) in [int, float, complex]:
            other = Matrix.fill(self.rows, self.columns, other)
        if not self.size == other.size:
            return None, 'Size mismatch'
        else:
            return Matrix([[base ** exponent
                            for base, exponent in
                            zip(self.content[row],
                                other.content[row])]
                           for row in range(self.rows)])

    def mul(self, other):
        """
        Associative, but not commutative.
        >>> print(Matrix([[1,3,2], [4,0,1]]).mul(Matrix([[1,3], [0,1], [5,2]])))
        [11, 10]
        [9, 14]

        >>> print(Matrix([[1,3], [2,4], [0,5]]).mul(Matrix([[1,0], [2,3]])))
        [7, 9]
        [10, 12]
        [10, 15]

        >>> print(Matrix([[1,0,0],[0,1,0],[0,0,1]]).mul(Matrix([[1],[3],[2]])))
        [1]
        [3]
        [2]

        >>> print(Matrix([[1,2],[3,4],[5,6]]).mul(Matrix([[11,12],[13,14],[15,16]])))
        (None, 'Size mismatch')
        
        >>> print(Matrix([[2,1],[3,4],[5,6]]).mul(Matrix([[1,3,6],[2,4,5]])))
        [4, 10, 17]
        [11, 25, 38]
        [17, 39, 60]

        >>> print(Matrix([[2,-2],[5,3]]).mul(Matrix([[-1,4],[7,-6]])))
        [-16, 20]
        [16, 2]

        >>> print(Matrix([[0,3,5],[5,5,2]]).mul(Matrix([[3,4],[3,-2],[4,-2]])))
        [29, -16]
        [38, 6]

        >>> print(Matrix([[-1,-2],[-2,-1]]).mul(Matrix([[2,0],[2,-1]])))
        [-6, 2]
        [-6, 1]

        >>> print(Matrix([[1,2],[-2,3]]).mul(Matrix([[0,-1,5],[3,2,1]])))
        [6, 3, 7]
        [9, 8, -7]

        >>> print(Matrix([[4,-1],[2,-1]]).mul(Matrix([[3,1,0],[2,1,-2]])))
        [10, 3, 2]
        [4, 1, 2]
        
        >>> import matrices, vectors
        >>> mat=matrices.Matrix([[1,2,1,5],[0,3,0,4],[-1,-2,0,0]])
        >>> vec=vectors.Vector([[1],[3],[2],[1]])
        >>> mat.mul(vec).show()
        [14]
        [13]
        [-7]

        >>> mat=matrices.Matrix([[1,0,3],[2,1,5],[3,1,2]])
        >>> vec=vectors.Vector([[1],[6],[2]])
        >>> mat.mul(vec).show()
        [7]
        [18]
        [13]

        >>> import matrices, vectors
        >>> mat=matrices.Matrix([[1,2104],[1,1416],[1,1534],[1,852]])
        >>> vec=vectors.Vector([[-40],[0.25]])
        >>> mat.mul(vec).show()
        [486.0]
        [314.0]
        [343.5]
        [173.0]

        >>> import matrices
        >>> mat=matrices.Matrix([[1,3],[2,4],[0,5]])
        >>> rix=matrices.Matrix([[1,0],[2,3]])
        >>> mat.mul(rix).show()
        [7, 9]
        [10, 12]
        [10, 15]

        >>> import matrices
        >>> mat=matrices.Matrix([[1,2104],[1,1416],[1,1534],[1,852]])
        >>> rix=matrices.Matrix([[-40,200,-150],[0.25,0.1,0.4]])
        >>> mat.mul(rix).show()
        [486.0, 410.4, 691.6]
        [314.0, 341.6, 416.4]
        [343.5, 353.4, 463.6]
        [173.0, 285.2, 190.8]

        >>> Matrix.eye(3).mul(Matrix([[1],[3],[2]])).show()
        [1]
        [3]
        [2]
        """
        if type(other) in [int, float, complex]:
            other = Matrix.fill(self.columns, self.rows, other)
        if type(other) == vectors.Vector:
            other = Matrix(other.content)
        if not self.columns == other.rows:
            return None, 'Size mismatch'

        return Matrix([[vectors.Vector(Matrix([self.content[row]]).transpose()
                                       .content).dot(other.vector(column))
                        for row in range(self.rows)]
                       for column in range(other.columns)]).transpose()

    ##        return Matrix([[mattor_dot([mat[row]], column(rix, column) )
    ##                                  for row in range(mat_size[0]) ]
    ##                                 for column in range(rix_size[1]) ] ).transpose()
    ##
    ##        return Matrix([[self.content[row][column] * other.content[column][row]
    ##                       for row in range(self.rows)]
    ##                       for column in range(other.columns)])

    def add(self, other):
        """
        >>> Matrix([[2, 2], [3, 3]]).add(Matrix([[2, 3], [2, 3]])).show()
        [4, 5]
        [5, 6]

        """
        if type(other) in [int, float, complex]:
            other = Matrix.fill(self.rows, self.columns, other)
        if not self.size == other.size:
            return None, 'Size mismatch'
        else:
            return Matrix([[self.content[row][column] +
                            other.content[row][column]
                            for column in range(self.columns)]
                           for row in range(self.rows)])

    def sub(self, other):
        """
        >>> Matrix([[2, 2], [3, 3]]).sub(Matrix([[2, 3], [2, 3]])).show()
        [0, -1]
        [1, 0]
        
        """
        if type(other) in [int, float, complex]:
            other = Matrix.fill(self.rows, self.columns, other)
        if not self.size == other.size:
            return None, 'Size mismatch'
        else:
            return Matrix([[self.content[row][column] -
                            other.content[row][column]
                            for column in range(self.columns)]
                           for row in range(self.rows)])

    def div(self, other):
        """
        >>> Matrix([[2, 2], [3, 3]]).div(Matrix([[2, 3], [2, 3]])).show()
        [1.0, 0.6666666666666666]
        [1.5, 1.0]

        """
        if type(other) in [int, float, complex]:
            other = Matrix.fill(self.rows, self.columns, other)
        if not self.size == other.size:
            return None, 'Size mismatch'
        else:
            return Matrix([[round(self.content[row][column] /
                                  other.content[row][column], 16)
                            if not (other.content[row][column]) == 0 else float("inf")
                            for column in range(self.columns)]
                           for row in range(self.rows)])

    def sum(self):
        """
        >>> print(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).sum())
        45
        """
        return sum([self.content[row][column]
                    for column in range(self.columns)
                    for row in range(self.rows)])

    def sum_corners(self):
        """
        >>> print(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).sum_corners())
        20
        """
        if (self.rows > 1) and (self.columns > 1):
            corners = [self.get(0, 0),
                       self.get(0, self.columns - 1),
                       self.get(self.rows - 1, 0),
                       self.get(self.rows - 1, self.columns - 1)]
            return sum(corners)
        else:
            return None

    def root(self):
        """
        >>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).root().show()
        [1.0, 1.414213562373095, 1.7320508075688772]
        [2.0, 2.23606797749979, 2.449489742783178]
        [2.6457513110645907, 2.82842712474619, 3.0]

        """
        return Matrix([[maths.sqrt(abs(self.content[row][column]))
                        for column in range(self.columns)]
                       for row in range(self.rows)])

    def sine(self):
        """
        >>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).sine().show()
        [0.8414709848078965, 0.9092974268256817, 0.1411200080598671]
        [-0.7568024953079275, -0.9589242746631357, -0.27941549819892936]
        [0.656986598718787, 0.9893582466234029, 0.41211848524190764]

        """
        return Matrix([[maths.sine(self.content[row][column])
                        for column in range(self.columns)]
                       for row in range(self.rows)])

    def cosine(self):
        """
        >>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).cosine().show()
        [0.5403023058681397, -0.41614683654714246, -0.9899924966004455]
        [-0.6536436208636125, 0.28366218546322675, 0.9601702866503709]
        [0.7539022543432953, -0.14550003380860246, -0.911130261884586]
        """
        return Matrix([[maths.cosine(self.content[row][column])
                        for column in range(self.columns)]
                       for row in range(self.rows)])

    def tangent(self):
        """
        >>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).tangent().show()
        [1.5574077246549023, -2.185039863261519, -0.1425465430742778]
        [1.1578212823495777, -3.380515006246586, -0.29100619138474915]
        [0.8714479827243188, -6.799711455220379, -0.45231565944180985]
        """
        return Matrix([[math.tan(self.content[row][column])
                        for column in range(self.columns)]
                       for row in range(self.rows)])

    def log(self):
        """
        >>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).log().show()
        [0.0, 0.6931471805599453, 1.0986122886681098]
        [1.3862943611198906, 1.6094379124341003, 1.791759469228055]
        [1.9459101490553132, 2.0794415416798357, 2.1972245773362196]

        """
        return Matrix([[math.log(abs(self.content[row][column]))
                        if not (self.content[row][column]) == 0 else float("NaN")
                        for column in range(self.columns)]
                       for row in range(self.rows)])

    def sqrt_inverse(self):
        """
        >>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).sqrt_inverse().show()
        [1.0, 0.7071067811865476, 0.5773502691896258]
        [0.5, 0.4472135954999579, 0.4082482904638631]
        [0.3779644730092272, 0.3535533905932738, 0.3333333333333333]

        """
        return Matrix([[1.0 / maths.sqrt(abs(self.content[row][column]))
                        if not (self.content[row][column]) == 0 else float("inf")
                        for column in range(self.columns)]
                       for row in range(self.rows)])
        # return Matrix([vectors.vector_inverse(column(self, column))
        # for column in range(self.columns)] )

    def invert(self):
        """
        Bad function, not to be used
        """
        return self.mul(Matrix.eye(self.rows))

    def fraction(self):
        """
        >>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).fraction().show()
        [1.0, 0.5, 0.3333333333333333]
        [0.25, 0.2, 0.16666666666666666]
        [0.14285714285714285, 0.125, 0.1111111111111111]

        """
        if not self.rows == self.columns:
            return None
        return Matrix([[1.0 / (abs(self.content[row][column]))  # pow((abs(matrix[row][column]), -1)
                        if not (self.content[row][column]) == 0 else float("inf")
                        for column in range(self.columns)]
                       for row in range(self.rows)])

    def exp(self):
        """
        >>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).exp().show()
        [2.718281828459045, 7.38905609893065, 20.085536923187668]
        [54.598150033144236, 148.4131591025766, 403.4287934927351]
        [1096.6331584284585, 2980.9579870417283, 8103.083927575384]

        """
        return Matrix([[math.exp(self.content[row][column])
                        for column in range(self.columns)]
                       for row in range(self.rows)])

    def absolute(self):
        """
        >>> Matrix([[-1, 2, -3], [4, -5, 6], [-7, -8, -9]]).absolute().show()
        [1, 2, 3]
        [4, 5, 6]
        [7, 8, 9]

        """
        return Matrix([[maths.absolute(self.content[row][column])
                        for column in range(self.columns)]
                       for row in range(self.rows)])

    def opposite(self):
        """
        >>> Matrix([[-1, 2, -3], [4, -5, 6], [-7, -8, -9]]).opposite().show()
        [-1, -2, -3]
        [-4, -5, -6]
        [-7, -8, -9]

        """
        return Matrix([[maths.opposite(self.content[row][column])
                        for column in range(self.columns)]
                       for row in range(self.rows)])

    def maximum(self):
        """
        >>> print(Matrix([[-1, 2, -3], [4, -5, 6], [-7, -8, -9]]).maximum())
        6
        """
        return max([(self.content[row][column])
                    for column in range(self.columns)
                    for row in range(self.rows)])

    def minimum(self):
        """
        >>> print(Matrix([[-1, 2, -3], [4, -5, 6], [-7, -8, -9]]).minimum())
        -9
        """
        return min([(self.content[row][column])
                    for column in range(self.columns)
                    for row in range(self.rows)])

    def morethan(self, target):
        """
        >>> print(Matrix([[-1, 2, -3], [4, -5, 6], [-7, -8, -9]]).morethan(5))
        [False, False, False]
        [False, False, True]
        [False, False, False]

        """
        return Matrix([[(self.content[row][column]) > target
                        for column in range(self.columns)]
                       for row in range(self.rows)])

    def lessthan(self, target):
        """
        >>> Matrix([[-1, 2, -3], [4, -5, 6], [-7, -8, -9]]).lessthan(5).show()
        [True, True, True]
        [True, True, False]
        [True, True, True]

        """
        return Matrix([[(self.content[row][column]) < target
                        for column in range(self.columns)]
                       for row in range(self.rows)])

    def equalto(self, target):
        """
        >>> Matrix([[-1, 2, -3], [4, 5, 6], [-7, -8, -9]]).equalto(5).show()
        [False, False, False]
        [False, True, False]
        [False, False, False]

        """
        return Matrix([[(self.content[row][column]) == target
                        for column in range(self.columns)]
                       for row in range(self.rows)])

    def find(self, target):
        """
        >>> print(Matrix(Matrix([[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]).lessthan(5)).find(True))
        [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2), (2, 2)]
        
        >>> print(Matrix(Matrix([[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]).morethan(5)).find(True))
        [(2, 1), (1, 2)]

        >>> print(Matrix(Matrix([[-1, 2, -3], [4, 5, 6], [-7, 8-3, -9]]).equalto(5)).find(True))
        [(1, 1), (2, 1)]

        >>> print(Matrix(Matrix.slide(10, 10)).find([5, -5]))
        [(5, 0), (6, 1), (7, 2), (8, 3), (9, 4), (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
        """
        if not type(target) == list:
            target = [target]
        return ([(row, column)
                 for column in range(self.columns)
                 for row in range(self.rows)
                 if self.content[row][column] in target])

    def dot(self, other):
        """
        >>> print(Matrix([[1,2],[3,4],[5,6]]).dot(Matrix([[11,12],[13,14],[15,16]])))
        301
        """
        if type(other) in [int, float, complex]:
            other = Matrix.fill(self.rows, self.columns, other)
        if not self.size == other.size:
            return None, 'Size mismatch'
        else:
            return sum([self.vector(column).dot(other.vector(column))
                        for column in range(self.columns)])

    def fill(rows, columns, value):
        """
        >>> Matrix.fill(3, 3, 9).show()
        [9, 9, 9]
        [9, 9, 9]
        [9, 9, 9]

        """
        return Matrix([[value for column in range(columns)]
                       for row in range(rows)])

    def sequence(start, stop, gap=1):
        """
        >>> x=Matrix.sequence(2,3,.25).stacked()
        >>> y=Matrix.sequence(-3,-4,-.3)
        >>> z=Matrix.mul(x,y).show()
        [-6.0, -6.6, -7.2, -7.8]
        [-6.75, -7.425, -8.1, -8.775]
        [-7.5, -8.25, -9.0, -9.75]
        [-8.25, -9.075, -9.9, -10.725]
        [-9.0, -9.899999999999999, -10.8, -11.7]
        >>> PiTau=Matrix.sequence(maths.GLOBAL_PI,maths.GLOBAL_TAU,math.pi).show()
        [3.141592653589793, 6.283185307179586]
        >>> PiTau=Matrix.sequence(maths.GLOBAL_PI,maths.GLOBAL_TAU,math.pi).mirror().show()
        [6.283185307179586, 3.141592653589793]
        >>> PiTau=Matrix.sequence(maths.GLOBAL_PI,maths.GLOBAL_TAU,math.pi).mirror().stacked().show()
        [6.283185307179586]
        [3.141592653589793]
        >>> PiTau=Matrix.sequence(maths.GLOBAL_PI,maths.GLOBAL_TAU,math.pi).mirror().stacked().flipped().show()
        [3.141592653589793]
        [6.283185307179586]
        >>> PiTau=Matrix.sequence(maths.GLOBAL_PI,maths.GLOBAL_TAU,math.pi).mirror().stacked().flipped().flatten().show()
        [3.141592653589793, 6.283185307179586]
        """
        if gap == 0.0:
            return Matrix([[start, stop]])
        if start == stop:
            return Matrix([[start, stop]])
        if gap < 0.0:
            start, stop = float(max(start, stop)), float(min(start, stop))
            seq = list([start])
            point = round(start + gap, 15)
            while not point < stop:
                seq.append(point)
                point = round(point + gap, 15)
        else:
            start, stop = float(min(start, stop)), float(max(start, stop))
            seq = list([start])
            point = round(start + gap, 15)
            while not point > stop:
                seq.append(point)
                point = round(point + gap, 15)
        return Matrix([seq])

    def zero(rows, columns):
        """
        >>> Matrix.zero(2, 5).show()
        [0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0]
        """
        return Matrix.fill(rows, columns, 0)

    def one(rows, columns):
        """
        >>> print(Matrix.one(5, 2))
        [1, 1]
        [1, 1]
        [1, 1]
        [1, 1]
        [1, 1]
        """
        return Matrix.fill(rows, columns, 1)

    def eye(rows):
        """
        >>> Matrix.eye(4).show()
        [1, 0, 0, 0]
        [0, 1, 0, 0]
        [0, 0, 1, 0]
        [0, 0, 0, 1]

        >>> Matrix([[-1, 2, -3], [4, -5, 6], [-7, -8, -9]]).mul(Matrix.eye(3) ).show()
        [-1, 2, -3]
        [4, -5, 6]
        [-7, -8, -9]

        >>> Matrix.eye(3).mul(Matrix([[-1, 2, -3], [4, -5, 6], [-7, -8, -9]] ) ).show()
        [-1, 2, -3]
        [4, -5, 6]
        [-7, -8, -9]
        """
        identity = Matrix.zero(rows, rows)
        for eye in range(rows):
            identity.content[eye][eye] = 1
        return Matrix(identity.content)

    def diagional(values):
        """
        >>> Matrix.diagional([2,4,6,8]).show()
        [2, 0, 0, 0]
        [0, 4, 0, 0]
        [0, 0, 6, 0]
        [0, 0, 0, 8]
        """

        rows = len(values)
        identity = Matrix.zero(rows, rows)
        for eye in range(rows):
            identity.content[eye][eye] = values[eye]
        return identity

    def identity(self):
        """
##        >>> Matrix([[1,2],[3,4],[5,6], [11,12],[13,14],[15,16]]).identity().show()
##        [5, 11, 17, 35, 41, 47]
##        [11, 25, 39, 81, 95, 109]
##        [17, 39, 61, 127, 149, 171]
##        [35, 81, 127, 265, 311, 357]
##        [41, 95, 149, 311, 365, 419]
##        [47, 109, 171, 357, 419, 481]

        >>> Matrix([[-1, 2, -3], [4, -5, 6], [-7, -8, -9]]).identity().show()
        [22, 16, -6]
        [-58, -31, 12]
        [158, 126, 78]
        """
        return self.mul(self.inverse() )

    def slide(rows, columns):
        """
        >>> Matrix.slide(4,3).show()
        [0, -1, -2]
        [1, 0, -1]
        [2, 1, 0]
        [3, 2, 1]
        """
        return Matrix([[row - column
                        for column in range(columns)]
                       for row in range(rows)])

    def random_float(rows, columns, lowest=0, highest=1):
        lowest, highest = (min(lowest, highest), max(lowest, highest))
        return Matrix([[lowest + random.random() * (highest - lowest)
                        for column in range(columns)]
                       for row in range(rows)])

    def random_whole(rows, columns, lowest=0, highest=100):
        lowest, highest = (min(lowest, highest), max(lowest, highest))
        return Matrix([[random.randint(lowest, highest)
                        for column in range(columns)]
                       for row in range(rows)])

    def random_binary(rows, columns):
        return Matrix.random_whole(rows, columns, 0, 1)

    def random_percent(rows, columns):
        return Matrix.random_whole(rows, columns, 0, 100)

    def histogram(self):
        values = {}
        for row in range(self.rows):
            for column in range(self.columns):
                ##                values[self.get(row, column)] = values[self.get(row, column)] + 1
                sample = self.get(row, column)
                if not sample in values:
                    values[sample] = 1
                else:
                    values[sample] = values[sample] + 1
        return values

    def join(self, other):
        """
        print(join(one(11,1), zero(11,11) ) )
        """
        if not self.rows == other.rows:
            return None, 'Size mismatch'
        else:
            return Matrix([self.content[row] + other.content[row]
                           for row in range(self.rows)])

    def insert_col(self, other, at):
        """
        print(insert_col(slide(11,11), zero(11,2), 7) )
        """
        if not self.rows == other.rows:
            return None, 'Size mismatch'
        else:
            return Matrix([self.content[row][:at] +
                           other.content[row] +
                           self.content[row][at:]
                           for row in range(self.rows)])

    def remove_col(self, at, cut=1):
        """
        print(remove_col(slide(11,11), 4, 3) ) )
        """
        if not ((self.columns >= at) and (self.columns >= at + cut)):
            return None, 'Size mismatch'
        else:
            return Matrix([self.content[row][0:at] +
                           self.content[row][at + cut:]
                           for row in range(self.rows)])

    def insert_row(self, other, at):
        """
        print(insert_row(slide(11,11), zero(2,11), 7) ) )
        """
        if not self.columns == other.columns:
            return None, 'Size mismatch'
        else:
            return Matrix(self.content[0:at] +
                          other.content +
                          self.content[at:])

    def remove_row(self, at, num=1):
        """
        print(remove_row(slide(11,11), 4, 3) ) )
        """
        if not ((self.rows >= at) and (self.rows >= at + num)):
            return None, 'Size mismatch'
        else:
            return Matrix(self.content[0:at] +
                          self.content[at + num:])

    def sort(self, backwards=False):
        self.content = [sorted(row, key=None, reverse=backwards)
                        for row in self.content]
        self.content = self.transpose().content
        self.content = [sorted(row, key=None, reverse=backwards)
                        for row in self.content]
        return self.transpose()

    def rotate(self, clockwise=True):
        """
        rotate(join(one(11,1), zero(11,11)),False)
        """
        if clockwise:
            return Matrix([list(element)
                           for element in
                           zip(*self.content[::-1])])
        else:
            return Matrix([list(element)
                           for element in
                           zip(*self.content[::-1])]).flipped().mirror()

    def shift(self, shift=1):
        if (shift % self.columns) == 0:
            return self
        return Matrix([self.content[row][shift % -self.columns:] +
                       self.content[row][:shift % self.columns]
                       for row in range(self.rows)])

    def cycle(self, cycle=1):
        return Matrix([self.content[row]
                       for row in range((cycle % -self.rows),
                                        (cycle % self.rows), 1)])

    def mirror(self):
        # mirror = zero(rows, columns)
        # for row in range(rows):
        # for column in range(columns):
        #        mirror[row][column - 1] = self.content[row][-column]
        return Matrix([self.content[row][::-1]
                       for row in range(self.rows)])

    def flipped(self):
        # return Matrix([self.content[-row -1] for row in range(self.rows)] )
        return Matrix(self.content[::-1])  # Clever method

    def flatten(self, vector=False):
        flat = []
        ##        for row in range(self.rows):
        ##            for column in range(self.columns):
        ##                flat.append(self.content[row][column])
        for row in range(self.rows):
            flat += self.content[row]
        if vector == True:
            return vectors.Vector([flat])
        else:
            return Matrix([flat])

    def stacked(self, vector=False):
        stack = []
        for column in range(self.columns):
            line = self.vector(column).content
            for row in range(self.rows):
                stack.append(line[row])
        if vector == True:
            return vectors.Vector(stack)
        else:
            return Matrix(stack)

    def reshape(self, newrows, newcols):
        """
        >>> Matrix([[9,8,7,6,5], [4,3,2,1,0], [0,1,2,3,4], [5,6,7,8,9]]).reshape(5,4).show()
        [9, 8, 7, 6]
        [5, 4, 3, 2]
        [1, 0, 0, 1]
        [2, 3, 4, 5]
        [6, 7, 8, 9]
        """
        feed = self.flatten()
        if not feed.columns == newrows * newcols:
            return self
        return Matrix([feed.element(0, segment * newcols, newcols)
                       for segment in range(newrows)])

    def capital(self):
        # rows, columns = measure(self)
        return self.join(Matrix.one(self.rows, 1))

    def determinant(self):
        """
        """
##        print("|", self.content[0][0], self.content[0][1], "|")
##        print("|", self.content[1][0], self.content[1][1], "|")
##        print(self.content[0][0] * self.content[1][1])
##        print(self.content[0][1] * self.content[1][0])
        return ((self.content[0][0] * self.content[1][1]) -
                (self.content[0][1] * self.content[1][0]))

    def reverse(self):
        """
        """
        #
        return self.mirror().flipped().transpose()

    def inverse(self):
        """
        >>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).inverse().show()
        [9, -2, -3]
        [-4, 5, -6]
        [-7, -8, 1]
        """
        if not self.rows == self.columns:
            return (None, 'Size mismatch')
        opposite = self.opposite()
        reverse = self.reverse()
        for eye in range(self.rows):
            opposite.content[eye][eye] = reverse.content[eye][eye]

##        inverted = opposite
##        return Matrix([[pow(inverted.content[row][column], -1)  # 1.0 / inverted[row][column]
##                        if not inverted.content[row][column] == 0 else float("inf")
##                        for column in range(self.columns)]
##                       for row in range(self.rows)])
        return opposite


    def normal_equation(self, vector):
        """
        Broken
        >>> ne = Matrix([ [2104,5,1,45], [1416,3,2,40], [1534,3,2,30], [852,2,1,36] ])
        >>> en = Matrix([[460],[232],[315],[178]])
        >>> ne.normal_equation(en).show()
        [55589478717]
        [-5822900841432]
        [-6285006755074]
        [-6718839396]
        """
        if not self.rows == vector.rows:
            return None, 'Size mismatch'
        capital = self.capital()
        # print("capital\n", capital)
        transpose = capital.transpose()
        # print("transpose\n", transpose)
        inversed = self.inverse()
        # print("inversed1\n", inversed)
        inversed = inversed.mul(capital)
        # print("inversed2\n", inversed)
        predictions = inversed.mul(transpose)
        # print("predictions\n", predictions)
        return predictions.mul(vector if type(vector) == Matrix
                               else Matrix(vector.content))

    def random_int(self, columns, param, param1):
        pass


transform_clockwise = Matrix([[0, 1], [-1, 0]])
transform_counterclockwise = Matrix([[0, -1], [1, 0]])

if __name__ == '__main__':
    doctest.testmod()
    unittest.main(exit=False)
