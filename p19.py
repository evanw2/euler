#!/usr/bin/env python


class Date(object):
   months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
   def __init__(self, month, day, year):
      self.day = day
      self.month = month
      self.year = year
   def month_days(self):
      if self.month != 2:
         return self.months[self.month]
      else:
         #leap year check
         y = self.year
         if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            return 29
         else:
            return 28
   def __cmp__(self, other):
      if self.year != other.year:
         return self.year - other.year
      elif self.month != other.month:
         return self.month - other.month
      else:
         return self.day - other.day
   def inc_week(self):
      self.day += 7
      m = self.month_days()
      if self.day > m:
         self.day = self.day - m
         self.month += 1
         if self.month > 12:
            self.month = 1
            self.year += 1
   


def pr_date(d):
   print d.month, d.day, d.year

#known sunday
d1 = Date(12,31,1899)

start = Date(1,1,1901)
end = Date(12,31,2000)

total = 0

while d1 < start:
   d1.inc_week()

while d1 <= end:
   if d1.day == 1:
      total += 1
   d1.inc_week()
   
print total




