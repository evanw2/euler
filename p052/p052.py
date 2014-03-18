#!/usr/bin/env python

"""
It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
contain the same digits.
"""

def same_digits(m, n):
   """Returns True if m and n cointain the same digits."""
   # Lists of digit counts
   lst1 = [0]*10
   lst2 = [0]*10
   while m > 0 and n > 0:
      lst1[m%10] += 1
      m /= 10
      lst2[n%10] += 1
      n /= 10
   if m != n: # both should be zero if same length
      return False
   return lst1 == lst2
   

def search():
   """ This simple approach ended up being faster than I expected."""
   n = 1
   while True:
      if same_digits(n, 2*n) and \
         same_digits(n, 3*n) and \
         same_digits(n, 4*n) and \
         same_digits(n, 5*n) and \
         same_digits(n, 6*n):
        return n
      n += 1

if __name__ == "__main__":
   print search()



