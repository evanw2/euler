#!/usr/bin/env python

def sum_fifths(n):
   total = 0
   while n > 0:
      total += (n%10)**5
      n = n/10
   return total

s = 0
for i in range(2,500000):
   if i == sum_fifths(i):
      s += i

print s



