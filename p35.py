#!/usr/bin/env python

"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

#returns true if array is a palindrome
def arr_pal(arr):
   i = 0
   j = len(arr)-1
   while i < j:
      if arr[i] != arr[j]:
         return False
      i += 1
      j -= 1
   return True

#returns true if n is a palindrome in base b
def pal(n, b):
   arr = []
   while n > 0: 
      arr.append(n%b)
      n = n/b
   return arr_pal(arr)
   

total = 0
for i in range(1,1000000):
   if pal(i,10) and pal(i,2):
      print i
      total += i

print total
   
