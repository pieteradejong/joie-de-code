import re
from collections import Counter
import unittest
import math


class TextFileParser:
    def get_line(self, filepath):
        with open(filepath, 'r') as f:
            for line in f:
                yield line.rstrip()

    def normalize(line):
        return line.lower()

    def strip_non_alpha_num(text):
        return re.compile(r'\W+', re.UNICODE).split(text)

    def entropy(self, string):
        p, lns = Counter(string), float(len(string))
        return -sum(count / lns * math.log(count / lns, 2) for count in p.values())


class Tests(unittest.TestCase):
    def set_up(self):
        pass

    def tear_down(self):
        pass

    def test_entropy(self):
        tfp = TextFileParser
        assertEquals(tfp.entropy("a"), 0)


if __name__ == "__main__":
    unittest.main()
