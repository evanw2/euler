#!/usr/bin/env python

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""

#only 10 factorials are needed:
factorial = [1,1,2,6,24,120,720,5040,40320,362880]

def digits(n):
   d = []
   while n > 0:
      d.append(n%10)
      n = n/10
   return d

def fact_digit(n):
   total = 0
   for d in digits(n):
      total += factorial[d]
   return total == n

total = 0
for i in range(3,2500000):
   if fact_digit(i):
      total += i

print total
   
