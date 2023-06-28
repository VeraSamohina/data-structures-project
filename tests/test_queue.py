import unittest
from src.queue import Queue, Node


class TestQueue(unittest.TestCase):
    def test_next_node(self):
        first = Node(1)
        second = Node(2, 1)
        third = Node(3, 2)
        self.assertEqual(first.next_node, None)
        self.assertEqual(second.next_node, 1)
        self.assertEqual(third.next_node, 2)

    def test_queue(self):
        queue1 = Queue()
        self.assertEqual(queue1.head, None)
        self.assertEqual(queue1.tail, None)
        queue1.enqueue('first')
        queue1.enqueue('second')
        self.assertEqual(queue1.head.data, 'first')
        self.assertEqual(queue1.tail.data, 'second')
        self.assertEqual(queue1.head.next_node.data, 'second')
        self.assertEqual(str(queue1), 'first\nsecond')


if __name__ == '__main__':
    unittest.main()
