#!/usr/bin/env python

#coin denominations
den = [200,100,50,20,10,5,2,1]

#cache - m[i][j] = num ways of making 
#matrix = []
#for i in range(10):
#   matrix.append([0,0,0,0,0,0,0,0])

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
  
