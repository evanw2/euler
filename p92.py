#!/usr/bin/env python

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



