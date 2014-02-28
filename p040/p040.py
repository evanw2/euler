#!/usr/bin/env python

"""

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

"""

#'state' variables
next_num = 1
# 1 - ones place, 2 - tens
current_digit = 1

def digits(n):
  total = 0
  while n > 0:
    n /= 10
    total += 1
  return total

#returns the next digit of the constant
def next():
  n = next_num
  m = current_digit
  while m > 1:
    n /= 10
    m -= 1
  return n % 10
  
#advances the state of the constant by a digit
def advance():
  global next_num
  global current_digit
  if current_digit > 1:
    current_digit -= 1
    return
  next_num += 1
  current_digit = digits(next_num)
  return
  
d0 = 1
for i in range(9):
  advance()
d1 = next()
for i in range(90):
  advance()
d2 = next()
for i in range(900):
  advance()
d3 = next()
for i in range(9000):
  advance()
d4 = next()
for i in range(90000):
  advance()
d5 = next()
for i in range(900000):
  advance()
d6 = next()

print d0 * d1 * d2 * d3 * d4 * d5 * d6

