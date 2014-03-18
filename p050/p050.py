#!/usr/bin/env python

import math

"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below 
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a 
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most 
consecutive primes?
"""


def prime_sieve_dict(upper):
   """ Returns an 'is_prime' dictionary for numbers less than upper """
   is_prime = {}

   for i in range(2, upper):
      is_prime[i] = True

   current_prime = 2
   while True:
      # Set all multiples of the current prime to be False.
      val = 2 * current_prime
      while val < upper:
         is_prime[val] = False 
         val += current_prime

      # get next prime, or break if it is outside the range
      val = current_prime + 1
      while val < upper and not is_prime[val]:
          val += 1
      if val == upper:
          break
      else:
          current_prime = val

   return is_prime    

prime_dict = prime_sieve_dict(1000000)

#Change dict to list
primes = [i for i in prime_dict.keys() if prime_dict[i]]


def find_consecutive(target, best_range):
   """Returns the max number of consecutive primes that
      can be used to generate n, or returns 0 if we cannot beat the
      'best range' passed in. It can be proved that
      the algorithm used here will not miss a consecutive
      sum for the target if one exists."""
   #L and R store the range of indicies we are looking at. 
   # (inclusive on Left, but not the Right.)
   L = 0
   R = 0
   total = 0
   while True:
      if(total) < target:
         if R == len(primes):
            break
         total += primes[R]
         R += 1
      elif total > target:
         if primes[L] * best_range > target:
            #cannot beat best range so far
            break
         total -= primes[L]
         L += 1
      else: # sum == target
         #we can return the first match we find, because
         # any further matches will have to use fewer primes,
         # since the primes are increasing in size
         return R - L
   return 0

def search():
   best = 0
   best_prime = 0
   i = 0
   for p in primes:
      i += 1
      c = find_consecutive(p, best)
      if c > best:
         best = c
         best_prime = p
   return (best, best_prime)

   
print search()[1]



