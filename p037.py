#!/usr/bin/env python

"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

def truncatable(n):
   digits = []
   digits.append(n%10)
   n = n/10
   while n > 0:
      if not is_prime(n):
         return False
      digits.append(n%10)
      n = n/10
   mult = 1
   for d in digits:
      n += d*mult
      if not is_prime(n):
         return False
      mult *= 10
   return True
      
num = 0
val = 8  
total = 0
while num < 11:
   if truncatable(val):
      total += val
      num += 1
   val += 1
      
print total
   
