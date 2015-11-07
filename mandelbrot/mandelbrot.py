# Author: Pieter de Jong

import random

def generateComplexNumber():
  random.seed()
  real = random.randint(-100, 100)
  compl = random.randint(-100, 100)
  c = (real, compl)
  return c


print(generateComplexNumber())
print(generateComplexNumber())

