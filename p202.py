#!/usr/bin/env python
import fractions

def valid(a,b):
   if a == 0 or b == 0:
      return False
   for i in range(1,min(a,b)):
      if a%i == 0 and b % i == 0:
         return False
   return True

surf = 12017639147
row = (surf + 3)/2
offset = 3 - (row %3)

col = offset
row -= offset


#total = 0
#while row > col:
#   if fractions.gcd(row,col) == 1:
#      total += 1
#   row -= 3
#   col += 3
#   if row %1000000 == 0:
#      print total, row
#
#print total * 2
   
total = 0
while row > col:
   if fractions.gcd(row,col) == 1:
      total += 1
   row -= 3
   col += 3
   if row %1000000 == 0:
      print total, row

print total * 2
