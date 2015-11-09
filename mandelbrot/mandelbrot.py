# Author: Pieter de Jong

import random
import pylab as pl

def generateComplexNumber():
  random.seed()
  real = random.randint(-100, 100)
  compl = random.randint(-100, 100)
  c = complex(real, compl)
  return c


def isMandelbrot(c):
  z = 0
  for i in range(100):
    z = pow(z, 2) + c
    absZ = abs(z)
    if absZ > 2:
      return False
  return True


def initExamples():
  Mandelbrot_yes = set()
  Mandelbrot_no = set()
  Mandelbrot_yes.add(complex(0,0))
  Mandelbrot_yes.add(complex(-1,0))
  Mandelbrot_yes.add(complex(-1.1,0))
  Mandelbrot_yes.add(complex(-1.3,0))
  Mandelbrot_yes.add(complex(-1.38,0))
  Mandelbrot_yes.add(complex(0,1))
  Mandelbrot_no.add(complex(1,0))
  Mandelbrot_no.add(complex(0,2))
  return Mandelbrot_yes, Mandelbrot_no




def runUnitTests():
  MYes, Mno = initExamples()
  print "Testing numbers which are in M set:"
  for z in MYes:
    if isMandelbrot(z) is True:
      print "PASSED"
    else:
      print "FAILED"
  
  print "Testing numbers which are NOT in M set:"
  for z in Mno:
    if isMandelbrot(z) is False:
      print "PASSED"
    else:
      print "FAILED"

  


  z = generateComplexNumber()
  print z
  isMandelbrot(z)
  z = generateComplexNumber()
  print z
  isMandelbrot(z)

  print isMandelbrot(complex(-1, 0))
  print isMandelbrot(complex(1, 0))

if __name__ == "__main__":
  runUnitTests()


