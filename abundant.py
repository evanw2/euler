#!usr/bin/env python


def num_divs(n):
   facts = prime_factors(n)
   divs = 1
   for key in facts:
      divs *= facts[key]+1
   return divs


def prime_factors(n):
   factors = {}
   for i in (primes + range(29, n+1)):
      if i > n:
         break
      while n % i == 0:
         if not i in factors:
            factors[i] = 0
         factors[i] += 1
         n /= i
   return factors

