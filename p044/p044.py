#!/usr/bin/env python

import time
import math
import timeit
from collections import OrderedDict

""""
Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten 
pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 
70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and 
difference are pentagonal and D = |Pk - Pj| is minimised; what is the value of D?
"""

#nth pentagonal number: n*(3n-1)/2
def p(n):
    return n*(3*n-1)/2


# Difference between P_(n+1) and P_n = 3n + 1

# Idea: Find minimum distance by scanning over numbers using distances of 
# increasing size starting at 1. We can tell when a distance can no longer
# be possible once the distance between neighboring pentagonal numbers is 
# greater than the current distance we are using. 

# Use a set to keep track of all the pentagonal numbers we know, adding
# more numbers when needed. The set is used to check if a number is pentagonal.

# Note -- it turns out this approach is more complicated and much slower than simply
# testing all pairs of pentagonal numbers under some fixed upper bound and
# repeatedly increasing that upper bound. I am leaving my bad solution here 
# though, since it took some time to write and is my own work.
# This code takes around an hour to run.

numbers = set()
for i in range(1,101):
    numbers.add(p(i))

max_gen = p(100)
max_index_generated = 100

def generate_more_numbers():
    #double the number of numbers we are storing in our dictionaries
    global max_index_generated
    global max_gen
    start = max_index_generated + 1
    end = max_index_generated * 2 + 1
    for i in range(start, end):
        numbers.add(p(i))
        
    max_index_generated *= 2
    max_gen = p(max_index_generated)


def is_pentagonal(k):
    global numbers
    while k > max_gen:
        generate_more_numbers()
    return k in numbers

    
class P_Num:
    """
    A very simple class for storing a pentagonal number that allows a client to
    easily increment to the next pentagonal number.
    """
    def __init__(self, value=1, index=1):
        self.value = value
        self.index = index

    def next(self):
        self.value += self.gap()
        self.index += 1

    def gap(self):
        """ Returns the distance between this number and the next pentagonal number"""
        # Difference between P_(n+1) and P_n = 3n + 1
        return self.index * 3 + 1


def search():
    # D is used to store the distance we are using to scan. 
    # D must be a pentagonal number, and look over all the other pentagonal
    #  numbers one by one.
    D = P_Num()
    #Using 'return' to break loop
    while True:
        n1 = P_Num()
        while D.value >= n1.gap:
            #print "D",D.value
            #print "n", n1.value
            n2 = n1.value + D.value
            if is_pentagonal(n2) and is_pentagonal(n1.value + n2):
                return (n1.value, D.value)
            n1.next()
        D.next()

        

print search()[1]


#These are functions I wrote to test a number for being pentagonal, but
# I decided that it might actually be faster just to make a set of known numbers.
def is_square(k):
    #check for some bit patterns for faster rejection
    last_3_bits = k & 7
    if not (last_3_bits == 0 or last_3_bits == 1 or last_3_bits == 4):
        return False
    d = round(math.sqrt(k))
    return d*d == k

# Solving the quadratic equation k = n(3n-1)/2 for n gives us:
#  n = (1 + sqrt(1 + 24k))/6
# If the above expression is an integer, then k is pentagonal.
def is_pentagonal2(k):
    if not is_square(1+24*k):
        return False
    return int(1 + math.sqrt(1+24*k)) % 6 == 0

