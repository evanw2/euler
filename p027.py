#!/usr/bin/env python

"""

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 
40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible
by 41.

The incredible formula  n^2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 
to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0.

"""


import math

def is_prime(n):
   if n < 2:
      return False
   if n == 2:
      return True
   i = 2
   sq = math.sqrt(n)
   while i <= sq:
      if n % i == 0:
         return False
      i += 1
   return True

#generate list of primes from 0 to 1000:
primes = []
for i in range(1000):
   if is_prime(i):
      primes.append(i)


def consec_primes(a,b):
   n = 0
   while is_prime( n*n + a*n + b ):
      n += 1
   return n
   

max_val = 0
max_a = 0
max_b = 0
#b must be prime
for b in primes:
   print b, max_val
   for a in range(-999,1000):
      c = consec_primes(a,b)
      if c > max_val:
         max_val = c
         max_a = a
         max_b = b
         
print "a,b:",max_a, max_b
print max_a * max_b
