import unittest
from src.stack import Stack, Node

class TestNode(unittest.TestCase):
    def test_next_node(self):
        one = Node(1)
        two = Node(2, 1)
        three = Node(3, 2)
        self.assertEqual(one.next_node, None)
        self.assertEqual(two.next_node, 1)
        self.assertEqual(three.next_node, 2)

class TestStack(unittest.TestCase):
    def test_stack(self):
        stack1 = Stack()
        with self.assertRaises(AttributeError):
            stack1.top.data, None
        stack1.push('ten')
        self.assertEqual(stack1.top.data, 'ten')

    def test_pop(self):
        stack2 = Stack()
        stack2.push('one')
        stack2.push('two')
        self.assertEqual(stack2.pop(), 'two')
        self.assertEqual(stack2.top.data, 'one')
        stack2.pop()
        self.assertEqual(stack2.top, None)
        self.assertEqual(stack2.pop(), None)

if __name__ == '__main__':
    unittest.main()
