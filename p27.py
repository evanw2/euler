#!/usr/bin/env python
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
