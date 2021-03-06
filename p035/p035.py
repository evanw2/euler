#!/usr/bin/env python
import math

"""

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

def digits(n):
   d = []
   while n > 0:
      d.append(n%10)
      n = n/10
   d.reverse()
   return d

def num_digits(n):
   total = 0
   while n > 0:
      total += 1
      n = n/10
   return total

def perms(n):
   d = num_digits(n)
   arr = []
   for i in range(d):
      arr.append(n)
      x = n % 10
      n = n/10
      n += x * 10**(d-1)
   return arr

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
      
#incorrect for n == 2
def is_c_prime(n):
   for d in digits(n):
      if d%2 == 0:
         return False
   for p in perms(n):
      if not is_prime(p):
         return False
   return True
   
total = 1
for i in range(3,1000000):
   if is_c_prime(i):
      total += 1

print total



