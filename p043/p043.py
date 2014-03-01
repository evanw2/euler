#!/usr/bin/env python


"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, 
we note the following:

d2 d3 d4  = 406 is divisible by 2
d3 d4 d5  = 063 is divisible by 3
d4 d5 d6  = 635 is divisible by 5
d5 d6 d7  = 357 is divisible by 7
d6 d7 d8  = 572 is divisible by 11
d7 d8 d9  = 728 is divisible by 13
d8 d9 d10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

# From divisibility constraints:
#   d4 = 0,2,4,6,8
#   d6 = 0,5

possible_digits = {1:set([1,2,3,4,5,6,7,8,9]),
                   2:set([0,1,2,3,4,5,6,7,8,9]),
                   3:set([0,1,2,3,4,5,6,7,8,9]),
                   4:set([0,2,4,6,8]),
                   5:set([0,1,2,3,4,5,6,7,8,9]),
                   6:set([0,5]),
                   7:set([0,1,2,3,4,5,6,7,8,9]),
                   8:set([0,1,2,3,4,5,6,7,8,9]),
                   9:set([0,1,2,3,4,5,6,7,8,9]),
                  10:set([0,1,2,3,4,5,6,7,8,9]) }


# I use recursive backtracking for this problem. I fill in the "board" 
# from right to left since the divisibility tests on the right side
# are less likely to be satisfied.

# the pandigital number itself is represented with a dictionary from
# position to digit, mostly
# because the problem statement gave me 1 based indexing, so I didn't
# want to confuse myself with 0 based indexing.


#concatenates 3 digits of number, starting at position i
def n(number, i):
    return 100*number[i] + 10*number[i+1] + number[i+2]

#converts dictionary representation to integer
def to_int(d):
    power = 1
    total = 0
    for i in range(10, 0, -1):
        total += d[i]*power
        power *= 10
    return total

#divisibility at 2 and 4 are automatically taken care of by possible_digits.
div_check_table = { 3:3, 5:7, 6:11, 7:13, 8:17 }
    
#the pandigital digits will be placed from right to left. Given 
# a position that we just placed a digit, performs the appropriate
# divisibility test.
def div_check(number, position):
    if position in div_check_table:
        #convert to 3 digit number, test for divisibility
        value = n(number, position)
        return value % div_check_table[position] == 0
    return True

results = []
unused_digits = set([0,1,2,3,4,5,6,7,8,9])

#recursive backtracking function to find numbers that work
def find_pandigitals(number, position):
    if position == 0:
        results.append(to_int(number))
        return
    digits = possible_digits[position] & unused_digits
    for digit in digits:
        number[position] = digit
        unused_digits.remove(digit)
        if div_check(number, position):
            find_pandigitals(number, position - 1)
        unused_digits.add(digit)

find_pandigitals({}, 10)

print sum(results)


