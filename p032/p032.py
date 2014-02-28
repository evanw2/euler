#!/usr/bin/env python

"""

We shall say that an n-digit number is pandigital if it makes use of all 
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""

#returns true if n could be part of a pandigital product
def possible(n):
   s = set()
   while n > 0:
      d = n%10
      if d == 0 or d in s:
         return False
      s.add(d)
      n /= 10
   return True

def pan(a,b,c):
   s = set()
   while a > 0:
      d = a%10
      if d == 0 or d in s:
         return False
      s.add( d )
      a = a/10
   while b > 0:
      d = b%10
      if d == 0 or d in s:
         return False
      s.add( d )
      b = b/10
   while c > 0:
      d = c%10
      if d == 0 or d in s:
         return False
      s.add( d )
      c = c/10
   return len(s) == 9
      

def pandigital(n):
   for i in range(2,n):
      if n%i == 0:
         if pan(n, i, n/i):
            return True
   return False
   

total = 0
#product will have to be 4 digits
for i in range(1234, 9877):
   if not possible(i):
      continue
   if pandigital(i):
      total += i

print total
   
   
