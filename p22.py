#!/usr/bin/env python

content = open("names.txt", "r").read()
names = content.replace('"', '').split(",")
names.sort()

def score(name):
   total = 0
   for c in name:
      total += ord(c) - ord('A') + 1
   return total
      
i = 1
total = 0
for name in names:
   total += score(name) * i
   i += 1

print total



