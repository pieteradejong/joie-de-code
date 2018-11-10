import unittest

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def get_head(self):
		return self.head

	def get_tail(self):
		return self.tail

	def add_to_head(self, value):
		pass

	def add_to_tail(self, value):
		pass

	def add_at_position(self, value):
		pass

	def get_node_by_position(self, value):
		pass

	def get_node_by_value_first(self, value):
		pass

	


class Node(object):
	def __init__(self, value = None, next = None):
		self.value = value
		self.next = next




class LinkedListTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass


def run_tests():
	ll = LinkedList()
	print ll


if __name__ == "__main__":
	run_tests()


