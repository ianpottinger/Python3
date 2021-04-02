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


#http://www.nyx.net/~gthompso/quine.htm

_='_=%r;print _(%%)_';print (_%_) 

print((lambda s:s%s)('print((lambda s:s%%s)(%r))'))

#python -c "x='python -c %sx=%s; print x%%(chr(34),repr(x),chr(34))%s'; print x%(chr(34),repr(x),chr(34))"


