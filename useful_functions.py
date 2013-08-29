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

##### Permutations methods ########

def maxed(digits):
   return sorted(digits, reverse = True) == digits

def largest_maxed(digits):
   i = len(digits) - 1
   while i > 0 and digits[i-1] > digits[i]:
      i = i-1
   return i
   #return digits[i::]

#return index of first digit from the right larger than n
def larger_than(digits, n):
   i = len(digits) - 1
   while i > 0 and digits[i] <= n:
      i = i-1
   return i

def swap(digits, i, j):
   tmp = digits[i]
   digits[i] = digits[j]
   digits[j] = tmp

#puts the digits past index i into increasing order
def sort_from_i(digits, i):
   digits[i:] = sorted(digits[i:])
      

def next(digits):
   if maxed(digits): 
      raise Exception('max')
   digit_to_move = largest_maxed(digits) - 1
   next_biggest = larger_than(digits, digits[digit_to_move])
   swap(digits, digit_to_move, next_biggest)
   sort_from_i(digits, digit_to_move + 1)
   
#############


def num_divs(n):
   facts = prime_factors(n)
   divs = 1
   for key in facts:
      divs *= facts[key]+1
   return divs


def prime_factors(n):
   factors = {}
   for i in range(2, n+1)):
      if i > n:
         break
      while n % i == 0:
         if not i in factors:
            factors[i] = 0
         factors[i] += 1
         n /= i
   return factors



