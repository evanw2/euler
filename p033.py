#!/usr/bin/env python

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""

from fractions import Fraction

#precondition: a and b are in the range [10,100]
def digit_cancel(a,b):
   num = [a/10, a%10]
   den = [b/10, b%10]
   if num[1] == den[0]:
      #(if a/b == c/d, then ad == bc)
      if b*num[0] == a*den[1]:
         return True
   #above case is actually the only possible case
   return False


a = 1
b = 1
for i in range(10,100):
   #denominator > numerator
   for j in range(i+1,100):
      if digit_cancel(i,j):
         a *= i
         b *= j

print Fraction(a,b).denominator
   
