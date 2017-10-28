import unittest

class MarkovFieldTest(unittest.TestCase):
    def setUp(self):
        print('In setUp()')
        self.fixture = range(1, 10)

    def tearDown(self):
        print('In tearDown()')
        del self.fixture


    def test(self):
        self.assertEqual(fun(3), 4)
        mkf = MarkovField()
        self.assertEqual