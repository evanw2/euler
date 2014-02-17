#!/usr/bin/env python

"""


If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""

def speak(n):
   ones = {1: "one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",
            7:"seven", 8:"eight", 9:"nine"}
   teens = {10: "ten", 11: "eleven", 12: "twelve", 13:"thirteen", 14:"fourteen",
            15: "fifteen", 16:"sixteen", 17: "seventeen", 18:"eighteen",
            19: "nineteen"}
   tens = { 2:"twenty ", 3:"thirty ", 4:"forty ", 5:"fifty ",
            6: "sixty ", 7: "seventy ", 8:"eighty ",9:"ninety "}
   str = ""
   if n > 9999:
      return "Too Big"
   if n > 999:
      th = n/1000
      str += ones[th] + " thousand "
   h = (n / 100)%10
   if h > 0:
      str += ones[h] + " hundred "
      if n % 100 != 0:
         str += "and "
   t = (n/10)%10
   if t == 1:
      str += teens[n%100]
      return str
   if t > 1 :
      str += tens[t]
   if n%10 != 0:
      str += ones[n%10]
   return str

def letters(s):
   sum = 0
   for c in s:
      if c != " ":
         sum += 1
   return sum



sum = 0
for i in range(1,1001):
   #print speak(i), letters(speak(i))
   sum += letters( speak(i) )

print sum
