#!/usr/bin/bash/env python

"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

"""

#python is ok with large numbers, which makes this easy
num = 2**1000
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num /= 10

print sum_digits

