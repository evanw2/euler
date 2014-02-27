#!/usr/bin/env python

"""

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?

"""

#returns the number of integer solutions for a right 
#  triangle of perimeter n
def int_sol(n):
  total = 0
  #hypotenuse must be at least equal to n*sqrt(2)/( 2 + sqrt(2) )
  #  which is about n*0.4142
  hyp = int(n*0.414)
  #hypotenuse must be less than n/2.
  while hyp < n/2:
    #check all possible values of a,b
    a = 1
    b = n - hyp - a
    while a < b:
      if a*a + b*b == hyp*hyp:
        total += 1
      a += 1
      b -= 1
    hyp += 1
  return total


# m, p = best number of solutions, best perimeter
m = 0
p = 0
for i in range(3,1000):
  n = int_sol(i)
  if n > m:
    m = n
    p = i

print p

