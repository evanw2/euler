#!/usr/bin/env python


import math
import operator as op


"""
Starting in the top left corner of a 2x2 grid, and only being
able to move to the right and down, there are exactly 6 routes
to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""


# nCr that avoids some of the factorial calculations
def nCr(n,r):
    #swap n-r and r to cancel as much as possible
    r = min(n-r, r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

#To get out of the grid, you will do down 20 times and right 20
#  times. The arrangements of these choices is 40 choose 20.

print nCr(40,20)


