#!/usr/bin/env python

def digits(n):
   total = 0
   while n > 0:
      total += 1
      n = n/10
   return total

index = 2
prev = 1
current = 1
while digits(current) < 1000:
   tmp = current
   current = current + prev
   prev = tmp
   index += 1

print index

