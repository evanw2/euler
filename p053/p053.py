
import operator as op

"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5_C_3 = 10.

In general,

nCr =	n! / r!(n-r)!
where r <= n, n! = n*(n-1)*...*3*2*1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23_C_10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, 
are greater than one-million?
"""


# nCr that avoids some of the factorial calculations
def nCr(n,r):
    #swap n-r and r to cancel as much as possible
    r = min(n-r, r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom


def main():
   count = 0
   for n in range(22,101): 
      for r in range(1,n):
         if nCr(n,r) > 1000000:
            count += 1
   print count
      
if __name__ == "__main__":
   main()

