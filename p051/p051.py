#!/usr/bin/env python

"""
By replacing the 1st digit of the 2-digit number *3, it turns out that 
six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 
5-digit number is the first example having seven primes among the ten 
generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 
56773, and 56993. Consequently 56003, being the first member of this 
family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not 
necessarily adjacent digits) with the same digit, is part of an eight 
prime value family.
"""

# keep prime dictionary global
is_prime = None

def search(upper_bound):
   initialize_prime_sieve_dict(upper_bound)
   p = 2
   while True:
      # Get next prime
      while not is_prime[p]:
         p += 1
         if p >= upper_bound:
            return False
      # positions is a list of numbers representing the 
      # places where we might swap out a digit
      L = num_digits(p)
      for i in range(1,2**L):
         # We can save some time by not checking the codes that
         #  don't end in 0. (They can't generate a large enough family)
         if i % 2 != 0:
            continue
         f = family_size(p, i)
         if f == 8:
            for j in range(10):
               if is_prime[swap(p,i,j)]:
                  return swap(p,i,j)
      p += 1



# Returns the family size of a number, given a code
# for what digits are being swapped out. The code is
# that the binary representation of the position code
# indicates which digits are to be swapped out
def family_size(n, position_code):
   L = num_digits(n) 
   if position_code >= 2**L:
      raise "Error"
   if position_code >= 2**(L-1):
      # we have to special case if the leading digit of n
      #  is being swapped, since we can't swap 0 into a leading digit.
      digits = [1,2,3,4,5,6,7,8,9]
   else:
      digits = [0,1,2,3,4,5,6,7,8,9]
      
   f_size = 0
   for digit in digits:
      swapped = swap(n, position_code, digit)
      if is_prime[swapped]:
         f_size += 1
   return f_size 

# replaces all the digits of n specified by the position code
# by the 'digit' parameter.
def swap(n, position_code, digit):
   # This sub-function swaps just the digit at position i
   def sw(i):
      # clear out the digit at position i
      cl = n%(10**i) + ( n//(10**(i+1)) )*(10**(i+1))
      return cl + (10**i)*digit
   position = 0
   while position_code > 0:
      if position_code % 2 > 0:
         # swap out at this position
         n = sw(position)
      position += 1
      position_code /= 2 
   return n
 
      
def num_digits(n):
   i = 0
   while n > 0:
      n = n // 10
      i += 1
   return i

def initialize_prime_sieve_dict(upper):
   """ creates the global dictionary"""
   global is_prime
   is_prime = {1: False}

   for i in range(2, upper):
      is_prime[i] = True

   current_prime = 2
   while True:
      # Set all multiples of the current prime to be False.
      val = 2 * current_prime
      while val < upper:
         is_prime[val] = False 
         val += current_prime

      # get next prime, or break if it is outside the range
      val = current_prime + 1
      while val < upper and not is_prime[val]:
          val += 1
      if val == upper:
          break
      else:
          current_prime = val



print search(1000000)



