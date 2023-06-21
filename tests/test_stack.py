import unittest
from src import stack

class TestNode(unittest.TestCase):
    def test_next_node(self):
        one = stack.Node(1)
        two = stack.Node(2, 1)
        three = stack.Node(3, 2)
        self.assertEqual(one.next_node, None)
        self.assertEqual(two.next_node, 1)
        self.assertEqual(three.next_node, 2)

class TestStake(unittest.TestCase):
    def test_stake(self):
        stack1 = stack.Stack()
        with self.assertRaises(AttributeError):
            stack1.top.data, None
        stack1.push('ten')
        self.assertEqual(stack1.top.data, 'ten')

if __name__ == '__main__':
    unittest.main()
