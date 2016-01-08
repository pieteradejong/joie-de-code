from collections import namedtuple
import numpy

class Perceptron:
  Sample = namedtuple('Sample', 'x y')

  def __init__(self, learning_rate=0.5):
    self.learning_rate = learning_rate

  def train(self, training_data): 
    '''
    training_data example: namedtuple('Labeled_Sample', 'x y')
    for each sample in training_data: sample.x is data, sample.y is label
    '''
    self.dim = len(training_data[0].x)
    self.initWeights(self.dim)
    for sample in training_data:
      y_prime = numpy.dot(self.weight_vector, sample.x)
      if self.sign(y_prime) != self.sign(sample.y) or y_prime == 0:
        adjustment = [self.learning_rate * sample.y * x for x in sample.x]
        self.weight_vector = [a + b for (a,b) in zip(self.weight_vector, adjustment)]

  def classify(self, sampleX):
    '''
    sampleX includes ONLY the sample.x (data) component of a sample,
    and NOT the label which would be sample.y
    '''
    dotprod = numpy.dot(self.weight_vector, sampleX)
    if dotprod > 0:
      return 1
    else:
      return 0

  def initWeights(self, dim):
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
    print "Testing training result:\n"
    print "Expect: \n", p.weight_vector, " to equal\n[0,1,0,-.5,.5]"

    print "\nTesting classification result:\n"
    print "Expect ", training_data[0].x, " to be classified as 1. Really: ", p.classify(training_data[0].x)
    print "Expect ", training_data[1].x, " to be classified as 0. Really: ", p.classify(training_data[1].x)
    print "Expect ", training_data[2].x, " to be classified as 1. Really: ", p.classify(training_data[2].x)
    print "Expect ", training_data[3].x, " to be classified as 0. Really: ", p.classify(training_data[3].x)
    print "Expect ", training_data[4].x, " to be classified as 1. Really: ", p.classify(training_data[4].x)
    print "Expect ", training_data[5].x, " to be classified as 0. Really: ", p.classify(training_data[5].x)


def testSign():
    print "Expect ", self.sign(-5), " to equal -1"
    print "Expect ", self.sign(0), " to equal 0"
    print "Expect ", self.sign(5), " to equal 1"

if __name__ == "__main__":
  testTraining()
