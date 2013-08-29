#!/usr/bin/env python



#started making this class, but didn't use it
class Lex(object):
   digits = [];
   def __init__(self, digs = None):
      if digs == None:
         for i in range(10):
            self.digits.append(i)
      else:
         for d in digs:
            self.digits.append(d)
   def __cmp__(self, other):
      for i in range(10):
         if self.digits[i] < other.digits[i]:
            return -1
         elif self.digits[i] > other.digits[i]:
            return 1
      return 0
   def __repr__(self):
      return str(digits)
      


def maxed(digits):
   return sorted(digits, reverse = True) == digits

def largest_maxed(digits):
   i = len(digits) - 1
   while i > 0 and digits[i-1] > digits[i]:
      i = i-1
   return i
   #return digits[i::]

#return index of first digit from the right larger than n
def larger_than(digits, n):
   i = len(digits) - 1
   while i > 0 and digits[i] <= n:
      i = i-1
   return i

def swap(digits, i, j):
   tmp = digits[i]
   digits[i] = digits[j]
   digits[j] = tmp

#puts the digits past index i into increasing order
def sort_from_i(digits, i):
   digits[i:] = sorted(digits[i:])
      

def next(digits):
   if maxed(digits): 
      raise Exception('max')
   digit_to_move = largest_maxed(digits) - 1
   next_biggest = larger_than(digits, digits[digit_to_move])
   swap(digits, digit_to_move, next_biggest)
   sort_from_i(digits, digit_to_move + 1)
   

d = [0,1,2,3,4,5,6,7,8,9]
for i in range(999999):
   next(d)


print d
   

      
      

