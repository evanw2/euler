#!/usr/bin/env python

def abundant(n):
   total = 0
   for i in range(1,n):
      if n %i == 0:
         total += i
   return total > n

nums = []

for n in range(1,28123):
   if abundant(n):
      nums.append(n)
sum2 = {}
for n in range(1,28123):
   sum2[n] = False

for num1 in nums:
   for num2 in nums:
      if num1 + num2 < 28123:
         sum2[num1 + num2] = True
         
total = 0
for n in range(1, 28123):
   if not sum2[n]:
      total += n

print total
      


