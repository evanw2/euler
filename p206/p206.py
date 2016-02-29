"""

 Find the unique positive integer whose square has the form
 1_2_3_4_5_6_7_8_9_0, where each "_" is a single digit.

"""

import math

match = [1,2,3,4,5,6,7,8]

upper_bound = int(math.sqrt(1929394959697989990))
lower_bound = int(math.sqrt(1020304050607080900))

# Checks if a number matches. As a slight optimization, 
# we skip checking the '9' and '0'  of the match due to 
# the way the numbers are being chosen.
def check_num(n):
  n = n//10000
  index = -1
  while n > 0:
    d = n%10
    if d != match[index]:
      return False
    index -= 1
    n = n/100
  return True

# We can reason out that the last digit is 0, 
# and the second to last digit is 3 or 7.

# This solution runs very quickly because the solution 
# happens to be very close to the upper bound.

n = upper_bound // 100
while True:
  n1 = 100*n + 30
  n2 = 100*n + 70
  if check_num(n1*n1):
    print n1
    break
  if check_num(n2*n2):
    print n2
    break
  n += 1


