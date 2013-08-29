#!/usr/bin/env python
import math

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

# Note: pandigitals with 8 or 9 digits are not prime

def is_pandigital(n):
   #assumed here that I wouldn't need to go below 7 digits
   s = set([1,2,3,4,5,6,7])
   while n > 0:
      d = n%10
      if d == 0 or d not in s:
         return False
      s.remove(d)
      n = n/10
   return True

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


n = 7654321
while True:
   if is_pandigital(n) and is_prime(n):
      break
   n -= 1
 
print n
   
