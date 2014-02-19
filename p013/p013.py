#!/usr/bin/env python

""""
 Work out the first ten digits of the sum of the following one-hundred
  50-digit numbers.
                       (numbers are in numbers.txt)
""""

f = open('numbers.txt')

total = 0
for line in f:
   total += int(line) 

#print first ten digits
print int(str(total)[:10])




