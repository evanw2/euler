#!/usr/bin/env python
primes = [2,3,5,7,11,13,17,19,23,29]

def tri(n):
   return n*(n+1)/2

def num_divs(n):
   facts = prime_factors(n)
   divs = 1
   for key in facts:
      divs *= facts[key]+1
   return divs
   #divs = 0
   #for i in range(1,n+1):
   #   if n % i == 0:
   #      divs += 1
   #return divs
def num_divs2(n):
   divs = 0
   for i in range(1,n+1):
      if n % i == 0:
         divs += 1
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

for i in range(9020, 90001):
   #print i,tri(i), num_divs( tri(i) ), prime_factors(tri(i))
   t = tri(i)
   if t % 30 == 0:
      n = num_divs( t )
      if n > 150:
         print i, t, n
         if n > 500:
            break

def is_prime(n):
   for i in range(2, n):
      if n % i == 0:
         return false
   return true


      
   
   
