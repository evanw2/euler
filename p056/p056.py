#!/usr/bin/env python

"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is 
the maximum digital sum?
"""

# An easy brute-force problem

def sum_digits(n):
   s = 0
   while n > 0:
      s += n % 10
      n /= 10
   return s

m = 0
for a in range(81, 100):
   for b in range(81, 100):
      m = max( m, sum_digits(a**b) )

print m

