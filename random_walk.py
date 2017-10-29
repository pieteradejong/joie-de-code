import random

def generate_Z():
  while True:
    yield random.choice([-1,1])

def generate_random_walk(steps):
  z = generate_Z()
  for _ in xrange(steps):
    print next(z, None)


generate_random_walk(100)
