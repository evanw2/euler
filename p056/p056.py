#!/usr/bin/env python

"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is 
the maximum digital sum?
"""

def sum_digits(n):
   s = 0
   while n > 0:
      s += n % 10
      n /= 10
   return s

# Statistically, it is very likely that a and b are both greater 
#   than 90, although it wouldn't take too long to check all 100^2
#   possibilities.

m = 0
for i in range(91, 100):
   for j in range(91, 100):
      s = sum_digits(i**j)
      if s > m:
         m = s

print m

