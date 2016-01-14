import random

class MarkovField:
  '''
  A Markov Random Field is a set of random variables
  having a Markov property described by an undirected graph.
  '''

  def __init__(self, ):
    self.graph = {}
    self.graph.A = {'A': 0.3, 'B': 0.7}
    self.graph.B = {'A': 0.1, 'B': 0.9}
    # todo: normalize: each node's outgoing edge probabilities sum to 1

  def run(self, steps):
    # states = self.graph.keys()
    current_state = random.choice(self.graph.keys())
    for i in range(steps):
      rando = random.random() # interval [0,1)
      # goal: pick next state
      possible_transitions = self.graph[current_state]
      for next_state in possible_transitions:
        probability = possible_transitions[next_state]
        
 

 