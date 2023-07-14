import unittest
from src.linked_list import LinkedList, Node


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node(1)

    def test_init(self):
        self.assertEqual(self.node.data, 1)
        self.assertEqual(self.node.next_node, None)


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_init(self):
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)

    def test_insert_beginning(self):

        self.list.insert_beginning({'value': 1})
        self.assertEqual(self.list.head.data, {'value': 1})
        self.assertEqual(self.list.tail.data, {'value': 1})
        self.assertIsNone(self.list.head.next_node)
        self.list.insert_beginning({'value': 2})
        self.assertEqual(self.list.head.data, {'value': 2})

    def test_insert_at_end(self):
        self.list.insert_at_end({'value': 2})
        self.assertEqual(self.list.head.data, {'value': 2})
        self.assertEqual(self.list.tail.data, {'value': 2})
        self.list.insert_at_end({'value': 3})
        self.assertEqual(self.list.head.data, {'value': 2})
        self.assertEqual(self.list.tail.data, {'value': 3})
        self.assertEqual(self.list.head.next_node.data, {'value': 3})

    def test_str(self):
        self.assertEqual(str(self.list), "None")
        self.list.insert_beginning({'value': 1})
        self.assertEqual(str(self.list), "{'value': 1} -> None")
        self.list.insert_at_end({'value': 2})
        self.assertEqual(str(self.list), "{'value': 1} -> {'value': 2} -> None")

    def test_to_list(self):
        self.list.insert_beginning({'value': 'two', 'id': 2})
        self.list.insert_beginning({'value': 'one', 'id': 1})
        self.assertEqual(self.list.to_list(), [{'value': 'one', 'id': 1}, {'value': 'two', 'id': 2}])

    def test_get_data_by_id(self):
        self.list.insert_beginning({'value': 'two', 'id': 2})
        self.list.insert_beginning({'value': 'one', 'id': 1})
        self.assertEqual(self.list.get_data_by_id(1), {'value': 'one', 'id': 1})


class RaiseTest(unittest.TestCase):
    def test_get_data_by_id_raise(self):
        self.list = LinkedList()
        self.list.insert_beginning([1, 2, 3])
        self.assertRaises(TypeError, self.list.get_data_by_id(2))


if __name__ == '__main__':
    unittest.main()
