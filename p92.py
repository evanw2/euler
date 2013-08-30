#!/usr/bin/env python

"""

A number chain is created by continuously adding the square of the digits in a number to form a new number 
until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is 
that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

"""

nums = {1:1, 89:89}

def sum_sq(i):
   total = 0
   while i > 0:
      total += (i%10)**2
      i = i/10
   return total
      

total = 0
for i in range(1,10000000):
   j = i
   while j not in nums:
      j = sum_sq(j)
   nums[i] = nums[j]
   if nums[i] == 89:
      total += 1
   

print total



