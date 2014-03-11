#!/usr/bin/env python

"""
The first two consecutive numbers to have two distinct prime 
factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct 
prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct 
prime factors. What is the first of these numbers?
"""

def make_factor_table(upper):
    """ Makes a factor table with upper bound. This table maps every
        value in the range [2, upper) to the number of distinct prime
        factors it has. The method used is similar to a prime sieve."""
    table = {}
    current_prime = 2
    while True:
        # increment all multiples of current_prime
        val = current_prime
        while val < upper:
            if val in table:
                table[val] += 1
            else:
                table[val] = 1
            val += current_prime

        # get next prime, or break if it is outside the range
        val = current_prime
        while val < upper and val in table:
            val += 1
        if val == upper:
            break
        else:
            current_prime = val

    return table    
        

#searches for k numbers with k distinct prime factors up to
# an upper bound of upper
def search(k, upper):
    table = make_factor_table(upper)
    streak = 0
    for value in range(2,upper):
        if table[value] == k:
            if streak == k - 1:
                #return first of the 4, not last
                return value - k + 1
            else:
                streak += 1
        else:
            streak = 0
    #'None' indicates that the search didn't find it in the range.
    return None
    
print search(4, 1000000)

               


#This method was used in a previous, slower version of the solution.
def num_distinct_fact(n):
    count = 0
    i = 2
    while i <= n:
        if n % i == 0:
            count += 1
            while n % i == 0:
                n = n / i
        i += 1
    return count

