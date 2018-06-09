"""
- need a few hash functions
- init params: m bits, k hashes
- can import existing hash functions?

"""

from bitarray import bitarray
import unittest
import mmh3
from fnvhash import fnv1a_32
import hashlib

class BloomFilter:
    def __init__(self, n):
        self.size = n
        self.array = [None] * self.size
        # self.hashes = [mmh3.hash, fnv1a_32, hashlib]
        self.hashes = [mmh3.hash]
    
    def add_string(self, s):
        for h in self.hashes:
            index = h(s) % self.size
            self.array[index] = True

    def is_present(self, s):
        for h in self.hashes:
            index = h(s) % self.size
            if not self.array[index]:
                return False
        return True

    
    def get_size(self):
        return self.size

    def get_approx_false_positive_rate(self):
        passdef


    def optimize_for_error_rate(self, n):
        passdef


class BloomFilterTest(unittest.TestCase):
    def setUp(self):
        print("Setting up...")
        self.bf = BloomFilter(10)

    def tearDown(self):
        # self.bf.dispose()
        self.bf = None

    def test_has_accurate_size(self):
        assert self.bf.get_size() == 10

    def test_item_not_added_is_not_present(self):
        assert self.bf.is_present('cofffee') is False

if __name__ == '__main__':
    unittest.main()