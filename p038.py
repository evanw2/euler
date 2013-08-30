#!/usr/bin/env python

"""

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 
1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the 
concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""

def is_9_pandigital(n):
   s = set([1,2,3,4,5,6,7,8,9])
   while n > 0:
      d = n%10
      if d not in s:
         return False
      s.remove(d)
      n = n/10
   return len(s) == 0

def concat(a,b):
   if b == 0:
      return a*10
   total = 0
   mult = 1
   while b > 0:
      total += (b%10)*mult
      mult *= 10
      b /= 10
   while a > 0:
      total += (a%10)*mult
      mult *= 10
      a /= 10
   return total
      
print "a"
print concat(92,45)
print concat(2,4995)
print "b"

#concatenated product of num with (1,2,..,n)
def concat_prod(num, n):
   total = num
   for i in range(2,n+1):
      total = concat(total, i*num)
   return total   

nums = [9,91,92,93,94,95,96]
ps = [2,3,4,5]

for n in nums:
   for m in ps:
      print concat_prod(n, m)
   
