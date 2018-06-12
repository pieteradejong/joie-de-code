import unittest

class LinkedList(object):
	def __init__(self):
		self.head = None

	def get_head(self):
		return self.head

	def get_tail(self):
		pass
		#TODO: walk to node that is tail

	def add_to_head(self, value):
		new_node = Node(value)
		new_node.next = self.get_head()
		self.head = new_node
		return get_head

	def add_to_tail(self, value):
		tail = self.get_tail()
		

	def add_at_position(self, pos):
		assert pos >= 0

		head = self.head()
		if not head:



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
		ll = LinkedList()

	def tearDown(self):
		ll = None

	def test_node_is_added_to_head(self):
		ll.add_to_head(4)
		assert ll.get_head().value == 4

	def test_node_is_added_to_tail(self):
		ll.add_to_tail(3)
		assert ll.get_tail().value == 3

	def test_add_at_position():
		ll.add_to_head(4)
		add_at_position()


def run_tests():
	ll = LinkedList()
	print ll


if __name__ == "__main__":
	run_tests()


