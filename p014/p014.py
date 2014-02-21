#!/usr/bin/env python

"""
The following iterative sequence is defined for the set of positive integers:
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) 
contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""


#Mapping from number to collatz chain length
collatz = {1:1}

def next_num(x):
    if x % 2 == 0:
        return x / 2
    else:
        return 3*x + 1

# Returns the length of the collatz chain starting at x. As
# a side effect, will add mappings to collatz dictionary.
def len_chain(x):
    if x in collatz:
        return collatz[x]
    else:
        x_chain = len_chain(next_num(x)) + 1
        collatz[x] = x_chain
        return x_chain

#find biggest starting value. The number 1 has chain length 1.
longest_start = 1
longest_chain = 1

for i in range(2,1000000):
    n = len_chain(i)
    if n > longest_chain:
        longest_chain = n
        longest_start = i

print longest_start, longest_chain


