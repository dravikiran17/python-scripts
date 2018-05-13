#!/usr/bin/python
def is_prime(x):
  if x < 2:
    return False
  if x == 2:
    return True
  for i in range(2,x,1):
    print i
    if(x%i == 0):
      return False
  else:
    return True
