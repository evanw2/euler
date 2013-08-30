#!/usr/bin/env python

"""

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 
2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 
6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""

#finds length of cycle in 1/n
def cycle(n):
   m = {1:1}
   r = 1
   i = 1
   while True:
      r = (r*10)%n
      i += 1
      if r in m:
         return i - m[r]
      else:
         m[r] = i
      

#returns fifty digits of 1/n
def print_frac(n):
   r = 1
   s = ""
   for i in range(50):
      s += str(r/n)
      r = r%n
      r = r*10
   return s

m = 1
ind = 1
for i in range(1,1000):
   c = cycle(i)
   if c > m:
      m = c
      ind = i

print ind
    
