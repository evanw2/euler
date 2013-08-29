#!/usr/bin/env python


from fractions import Fraction

seq = [2]
for i in range(33):
   seq.append(1)
   seq.append((i+1)*2)
   seq.append(1)
   

#turns a continued fraction into a single fraction
def compress(expanded):
   f = Fraction(expanded[-1],1)
   for e in reversed(expanded[:-1]):
      f = 1/f
      f = f+Fraction(e,1)
   return f

def sum_digits(n):
   total = 0
   while n > 0:
      total += n%10
      n = n/10
   return total


print sum_digits(compress(seq).numerator)
      
      


