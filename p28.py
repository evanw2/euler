#!/usr/bin/env python

total = 1
squares = 500
sq_len = 2
n = 1
while squares > 0:
   #process next square
   for i in range(4):
      n += sq_len
      total += n
   sq_len += 2
   squares -= 1

print total


