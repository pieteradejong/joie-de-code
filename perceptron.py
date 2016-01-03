from collections import namedtuple
import numpy

class Perceptron:
  Sample = namedtuple('Sample', 'x y')

  def __init__(self, learning_rate=0.5):
    self.learning_rate = learning_rate

  def train(self, training_data): 
    # method accepts list of named tuples with sample.x (itself a list) and sample.y
    # e.g. namedtuple('Labeled_Sample', 'x y')
    self.dim = len(training_data[0].x)
    self.init_weights(self.dim)
    for sample in training_data:
      y_prime = numpy.dot(self.weight_vector, sample.x)
      if self.sign(y_prime) != self.sign(sample.y) or y_prime == 0:
        adjustment = [self.learning_rate * sample.y * x for x in sample.x]
        self.weight_vector = [a + b for (a,b) in zip(self.weight_vector, adjustment)]
        print self.weight_vector

  def classify(self, sampleX):
    # sampleX only includes the x component of a sample
    dotprod = numpy.dot(self.weight_vector, sampleX)
    if dotprod > 0:
      return 1
    else:
      return 0

  def init_weights(self, dim):
    self.weight_vector = [0] * dim

  def setLearningRate(self, number): 
    self.learning_rate = number
  
  def sign(self, number):
    if number < 0:
      return -1
    if number > 1:
      return 1
    return 0

def testTraining():
    p = Perceptron()
    training_data = [
      p.Sample(x=[1,1,0,1,1],y=1),
      p.Sample(x=[0,0,1,1,0],y=-1),
      p.Sample(x=[0,1,1,0,0],y=1),
      p.Sample(x=[1,0,0,1,0],y=-1),
      p.Sample(x=[1,0,1,0,1],y=1),
      p.Sample(x=[1,0,1,1,0],y=-1)
    ]
    p.train(training_data)
    print "\nTesting training result:\n"
    print "Expect ", p.weight_vector, " to equal [0,1,0,-.5,.5]"
    print "\n"

    print "Testing classification result:\n"
    print "Expect ", training_data[0].x, " to be classified as +1. Really: ", p.classify(training_data[0].x)
    print "Expect ", training_data[1].x, " to be classified as 0. Really: ", p.classify(training_data[1].x)
    print "Expect ", training_data[2].x, " to be classified as +1. Really: ", p.classify(training_data[2].x)
    print "Expect ", training_data[3].x, " to be classified as 0. Really: ", p.classify(training_data[3].x)
    print "Expect ", training_data[4].x, " to be classified as +1. Really: ", p.classify(training_data[4].x)
    print "Expect ", training_data[5].x, " to be classified as 0. Really: ", p.classify(training_data[5].x)


def testSign():
    print "Expect ", self.sign(-5), " to equal -1"
    print "Expect ", self.sign(0), " to equal 0"
    print "Expect ", self.sign(5), " to equal 1"

if __name__ == "__main__":
  testTraining()
