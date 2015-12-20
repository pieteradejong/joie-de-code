import numpy

class Perceptron:
  def __init__(self):
    self.learning_rate = 0.5
    self.weight_vector = [0,0,0,0,0] # start with dim = 5
    self.training_data = [
      [1,1,0,1,1,1],
      [0,0,1,1,0,-1],
      [0,1,1,0,0,1],
      [1,0,0,1,0,-1],
      [1,0,1,0,1,1],
      [1,0,1,1,0,-1]
    ]

  def train(self):
    for sample in self.training_data:
      y_prime = numpy.dot(self.weight_vector, sample[:len(sample)-1])
      if self.sign(y_prime) != self.sign(sample[-1]) or y_prime == 0:
        adjustment = [self.learning_rate * sample[-1] * x for x in sample[:len(sample)-1]]
        self.weight_vector = [a + b for (a,b) in zip(self.weight_vector, adjustment)]
        print self.weight_vector

  def setLearningRate(self, number):
    self.learning_rate = number

  def sign(self, number):
    if number < 0:
      return -1
    if number > 1:
      return 1
    return 0

if __name__ == "__main__":
  p = Perceptron()
  p.train()

# ideas: 
# parametrize dim
# learning rate as arg
# refactor y
# create a few testcases

# API should be :

# import Percepton
# p = Perceptron()
# p.setLearningRate(0.1)
# p.initializeWeights()
# p.train(samples)
# p.classify(example)

# python perceptron.py
# [use cmd line args]







