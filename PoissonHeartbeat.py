import time
import random

class PoissonHeartbeat:
  def __init__(self, runtime=10):
    self.lambd = 0.1
    intervals = [random.expovariate(self.lambd) for i in range(runtime)]
    print intervals
    for v in intervals:
      time.sleep(v)
      print "ping! after interval ", v

if __name__ == "__main__":
  phb = PoissonHeartbeat()

