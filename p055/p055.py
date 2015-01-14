#!/usr/bin/env python

"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers,
like 196, never produce a palindrome. A number that never forms a 
palindrome through the reverse and add process is called a Lychrel 
number. Due to the theoretical nature of these numbers, and for the 
purpose of this problem, we shall assume that a number is Lychrel 
until proven otherwise. In addition you are given that for every 
number below ten-thousand, it will either (i) become a palindrome in 
less than fifty iterations, or, (ii) no one, with all the computing 
power that exists, has managed so far to map it to a palindrome. In 
fact, 10677 is the first number to be shown to require over fifty 
iterations before producing a palindrome: 4668731596684224866951378664 
(53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves 
Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

"""

# Avoid recomputing the same lychrel numbers
lychrel_cache = {}

def is_palindrome(n):
   digits = []
   while n > 0:
      digits.append(n%10)
      n = n/10
   i = 0
   j = len(digits)-1
   while i < j:
      if digits[i] != digits[j]:
         return False
      i += 1
      j -= 1
   return True

def rev(n):
   m = 0
   while n > 0:
      m *= 10
      m += n % 10
      n /=10
   return m

def is_lychrel(n, i):
   if n in lychrel_cache:
      return lychrel_cache[n]
   if i > 50:
      return True
   # reverse and add n to itself
   m = n + rev(n)
   if is_palindrome(m):
      lychrel_cache[n] = False
      return False
   else:
      L = is_lychrel(m, i+1 )
      lychrel_cache[n] = L
      return L

count = 0
for i in range(10001):
   if is_lychrel(i,0):
      count += 1
   
print count

