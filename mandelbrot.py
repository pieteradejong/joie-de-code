# Author: Pieter de Jong

import random

def generateComplexNumber():
  random.seed()
  real = random.randint(-100, 100)
  compl = random.randint(-100, 100)
  c = complex(real, coml)
  return c


def isMandelbrot(c):
  z = 0
  for i in range(100):
    z = pow(z, 2) + c
    absZ = abs(z)
    if absZ > 2:
      return False
  print "Is Mandelbrot!"
  return True





# z = generateComplexNumber()
# print z
# isMandelbrot(z)
# z = generateComplexNumber()
# print z
# isMandelbrot(z)

print isMandelbrot(complex(-1, 0)
