
"""
It is possible to show that the square root of two can be expressed as 
an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

   1 + 1/2 = 3/2 = 1.5
   1 + 1/(2 + 1/2) = 7/5 = 1.4
   1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
   1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

   The next three expansions are 99/70, 239/169, and 577/408, but the 
   eighth expansion, 1393/985, is the first example where the number of 
   digits in the numerator exceeds the number of digits in the denominator.

   In the first one-thousand expansions, how many fractions contain a 
   numerator with more digits than denominator?
"""


import fractions

def recip((a, b)):
  return (b,a)

def plustwo((a,b)):
  return (2*b+a, b)

def plusone((a,b)):
  return (b+a, b)

def reduce((a,b)):
  g = fractions.gcd(a,b)
  return (a/g,b/g)

def next(x):
  return reduce(recip(plustwo(x)))

def numdigits(n):
  d = 0
  while n > 0:
    n = n/10
    d += 1
  return d

def test((a,b)):
  return numdigits(a) > numdigits(b)

val = (1,2)
count = 0

for i in range(1000):
  res = plusone(val)
  if test(res):
    count += 1

  val = next(val)

print count


