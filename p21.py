#!/usr/bin/env python

def d(n):
   total = 0
   for i in range(1,n):
      if n%i == 0:
         total += i
   return total


total = 0
for i in range(1,10000):
   if d(i) != i and d(d(i)) == i:
      total += i
print total
   



