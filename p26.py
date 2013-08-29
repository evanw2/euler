#!/usr/bin/env python

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

print cycle(999)
print ind,m
    
