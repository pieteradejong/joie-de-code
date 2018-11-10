import random


class MarkovField:
    '''
    A Markov Random Field is a set of random variables
    having a Markov property described by an undirected graph.
    '''

    def __init__(self):
        self.graph = {}
        self.graph['A'] = {'A': 0.5, 'B': 0.5}
        self.graph['B'] = {'A': 0.5, 'B': 0.5}
        self.states = self.graph.keys()
        # todo: normalize: each node's outgoing edge probabilities sum to 1

    def run(self, steps=10):
        # TODO: specify probability distribution for initial state (could be indicator func)
        current_state = random.choice(self.states)
        print
        "Randomly selected initial state:", current_state
        for i in range(steps):
            rando = random.random()  # interval [0,1)
            # goal: pick next state
            possible_transitions = self.graph[current_state]
            cumulative_probability = 0
            for next_state in possible_transitions:
                probability = possible_transitions[next_state]
                cumulative_probability += probability
                if rando < cumulative_probability:
                    current_state = next_state
                    print
                    "Next state: ", next_state
                    break
