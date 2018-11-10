import time
import random


class PoissonHeartbeat:
    def __init__(self, numberOfEvents=10, lambd=0.1):
        self.numberOfEvents = numberOfEvents
        self.lambd = lambd
        intervals = [random.expovariate(self.lambd) for i in range(self.numberOfEvents)]
        print
        intervals, "\n"
        for v in intervals:
            time.sleep(v)
            print
            "ping! after interval ", v


if __name__ == "__main__":
    phb = PoissonHeartbeat()
