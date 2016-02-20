import math

def is_prime(n):
   i = 2
   sq = math.sqrt(n)
   while i <= sq:
      if n % i == 0:
         return False
      i += 1
   return True

# Initialize to a 3x3 square
total_diag = 5
total_prime = 3
d1 = [3]
d2 = [5]
d3 = [7]
sq_len = 3

# Expand the square
while True:
  d1_next = d1[-1] + 2*(sq_len - 1) + 2*(sq_len + 0)
  d2_next = d2[-1] + 1*(sq_len - 1) + 2*(sq_len + 0) + 1*(sq_len + 1)
  d3_next = d3[-1] + 2*(sq_len + 0) + 2*(sq_len + 1)
  for n in [d1_next, d2_next, d3_next]:
    if is_prime(n):
      total_prime += 1
  d1.append(d1_next)
  d2.append(d2_next)
  d3.append(d3_next)
  sq_len += 2
  total_diag += 4

  if 1.0*total_prime/total_diag < 0.1:
    break
  
print sq_len

