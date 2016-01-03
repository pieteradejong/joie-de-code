# joie-de-code
for the love of writing code

<i>joie de vivre</i> noun, French. meaning: joy of living

Perceptron:
- most Perceptron properties, including data dimensionality, are determined at training
- learning rate is set to a default in the constructor, and can either be overridden there or 
later with a setter
- train method takes a list of namedtuples, with both an x (data) and y (label) component
- Usage: 
-- import Perceptron
-- p.setLearningRate(0.1) # optional
-- p.train(samples)
-- p.classify(sample)

