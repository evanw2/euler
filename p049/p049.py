#!/usr/bin/env python

import math

# range of possible starting values: odd #s in 1001 - 9997
#  (could be narrowed more)
# possible increments:  even numbers in range 2 - 4000
#  (could be narrowed more)

prime_cache = {2:True}

def is_prime(n):
   if n in prime_cache:
      return prime_cache[n]
   i = 2
   sq = math.sqrt(n)
   while i <= sq:
      if n % i == 0:
         prime_cache[n] = False
         return False
      i += 1
   prime_cache[n] = True
   return True


def next_prime(n):
   """This function assumes the input is odd."""
   m = n + 2
   while not is_prime(m):
      m += 2
   return m

def digits(v):
   """returns the counts of digits in v, if v is written
      as a 4 digit number in base 10."""
   d = {}
   for i in range(4):
      digit = v%10
      if digit in d:
         d[digit] += 1
      else:
         d[digit] = 1
      v /= 10
   return d


def test(v, inc):
   """Tests the values for the property we are looking for.
       v already should be prime."""
   if v + 2*inc > 9999:
      return False
   if not is_prime(v + inc):
      return False
   if not is_prime(v + 2*inc):
      return False
   # check permutations 
   d1 = digits(v)
   d2 = digits(v + inc)
   d3 = digits(v + 2*inc)
   return d1 == d2 and d2 == d3


def search():
   v = next_prime(999)
   while v < 10000:
    # (Progress bar)
    #  if v %1000 == 0:
    #     print v
      #try all possible increments
      inc = 2
      while inc < 4000:
         if test(v, inc) and v != 1487:
            return str(v) + str(v+inc) + str(v+2*inc)
         inc += 2
      v = next_prime(v)
   return "No solution?"
      

print search()


