#!/usr/bin/env python

"""

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

"""

#coin denominations
den = [200,100,50,20,10,5,2,1]

cache = {}

#returns the number of ways of making n pence
# using den >= index i
def ways(n, i):
  if (n,i) in cache:
    return cache[(n,i)]
  if n == 0:
    return 1
  if n < 0 or i >= len(den):
    return 0
  if i == len(den)-1:
    return 1
  total = 0
  m = n
  while m >= 0:
    total += ways(m, i+1)
    m -= den[i]
  cache[(n,i)] = total
  return total
  

print ways(200,0)
  
