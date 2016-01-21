# joie-de-code
for the love of writing code

<i>joie de vivre</i> noun, French. meaning: joy of living

# Markov Chain
- Markov Chains processes work as follows:
-- Markov Chains are fully specified by a set of states and the transition probabilities between each state and each other state (often represented by a matrix)
-- the Markov process starts in one of these states, chosen according to some probabilty distribution
-- on each "step", the process *transitions* from its current state to a subsequent state, potentially the same state
- Interestingly, there exists the following theorem:
-- Let P be the transition matrix of a Markov Chain. The ijth entry p_ij^n of the matrix P^n gives the probability that the Markov chain, starting at state s_i, will be in state s_j after n steps. (Wherein P^n = P x P x P x P ... (n times)

## TODO:
### API:
- infer set of states from transition matrix specified at initialization
## Features needed for interesting applications / questions we might ask:


# Perceptron:
- most Perceptron properties, including data dimensionality, are determined at training
- learning rate is set to a default in the constructor, and can either be overridden there or 
later with a setter
- train method takes a list of namedtuples, with both an x (data) and y (label) component
- Usage: 
-- import Perceptron
-- p.setLearningRate(0.1) # optional
-- p.train(samples)
-- p.classify(sample)

# PoissonHeartBeat:
- The Poisson probability distribution was developed by the French mathematician Simeon Denis Poisson in 1837
- A key term related to 
- A Poisson random variable satisfies the following conditions:
-- The number of events in two disjoint time intervals is independent
- The Poission probability distribution is given by:
-- [TODO: insert math]


## Applications of the Poisson process
- machine life time modeling





