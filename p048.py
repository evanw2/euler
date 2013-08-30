#!/usr/bin/env python

"""

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""

#almost feels like using Python is cheating for this one...

total = 0

for i in range(1,1000):
   total += i**i

print total%10000000000
   
