#!/usr/bin/env python

import math

"""
 It was proposed by Christian Goldbach that every odd composite 
 number can be written as the sum of a prime and twice a square.
 
 9 = 7 + 2x12
 15 = 7 + 2x22
 21 = 3 + 2x32
 25 = 7 + 2x32
 27 = 19 + 2x22
 33 = 31 + 2x12
 
 It turns out that the conjecture was false.
 
 What is the smallest odd composite that cannot be written as 
 the sum of a prime and twice a square?
"""

def is_prime(n):
   if n == 2:
      return True
   if n < 2 or n % 2 == 0:
      return False
   i = 2
   sq = math.sqrt(n)
   while i <= sq:
      if n % i == 0:
         return False
      i += 1
   return True

def sum_of_prime_and_2sq(n):
   #test all possible squares
   sq = 1
   sq_i = 1
   while 2*sq < n:
      if is_prime(n - 2*sq):
         return True
      sq += 2*sq_i + 1
      sq_i += 1
   return False

def search():
   val = 1
   while True:
       val += 2
       if not is_prime(val):
           if not sum_of_prime_and_2sq(val):
               return val
    
print search()

