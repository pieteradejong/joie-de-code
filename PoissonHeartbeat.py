import time
import random

class PoissonHeartbeat:
  def __init__(self, events=10, lambd=0.1):
    self.events = events
    self.lambd = lambd
    intervals = [random.expovariate(self.lambd) for i in range(self.events)]
    print intervals, "\n"
    for v in intervals:
      time.sleep(v)
      print "ping! after interval ", v

if __name__ == "__main__":
  phb = PoissonHeartbeat()

