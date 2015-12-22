import unittest
import doublylinkedlist


class DLL_Test(unittest.TestCase):
    def test_create_dll(self):
        dll = doublylinkedlist.LinkedList()
        self.assertEqual(dll.head, None)
        self.assertEqual(dll.tail, None)
        self.assertEqual(dll.count, 0)

    def test_add_first(self):
        dll = doublylinkedlist.LinkedList()
        dll.add(1)
        self.assertEqual(dll.head.data, 1)
        self.assertEqual(dll.head.next, None)
        self.assertEqual(dll.head.prev, None)
        self.assertEqual(dll.count, 1)

    def test_add_second(self):
        dll = doublylinkedlist.LinkedList()
        dll.add(1)
        node_1_head = dll.head
        dll.add(2)
        self.assertEqual(dll.head.data, 2)
        self.assertEqual(dll.head.next, node_1_head)
        self.assertEqual(dll.head.prev, None)
        self.assertEqual(dll.count, 2)

    def test_size(self):
        dll = doublylinkedlist.LinkedList()
        dll.add(1)
        dll.add(2)
        dll.add(3)
        self.assertEqual(dll.size(), 3)

    def test_size_when_ll_is_none(self):
        dll = doublylinkedlist.LinkedList()
        self.assertEqual(dll.size(), 0)

    def test_peek_head(self):
        dll = doublylinkedlist.LinkedList()
        dll.add(1)
        dll.add(2)
        dll.add(3)
        self.assertEqual(dll.peek_head(), 3)

    def test_peek_head_when_ll_is_none(self):
        dll = doublylinkedlist.LinkedList()
        self.assertRaises(Exception, dll.peek_head)

    def test_peek_tail(self):
        dll = doublylinkedlist.LinkedList()
        dll.add(1)
        dll.add(2)
        dll.add(3)
        self.assertEqual(dll.peek_tail(), 1)

    def test_peek_tail_when_ll_is_none(self):
        dll = doublylinkedlist.LinkedList()
        self.assertRaises(Exception, dll.peek_tail)

    def test_pop_head_when_head_is_none(self):
        dll = doublylinkedlist.LinkedList()
        self.assertRaises(Exception, dll.pop_head)

    def test_pop_head_when_head_is_one_node(self):
        dll = doublylinkedlist.LinkedList()
        dll.add(1)
        self.assertEqual(dll.head, dll.tail)
        self.assertEqual(dll.pop_head(), 1)
        self.assertEqual(dll.head, None)
        self.assertEqual(dll.count, 0)

    def test_pop_head_when_head_is_more_than_one_node(self):
        dll = doublylinkedlist.LinkedList()
        dll.add(1)
        dll.add(2)
        dll.add(3)
        dll.add(4)
        self.assertEqual(dll.pop_head(), 4)
        self.assertEqual(dll.head.data, 3)
        self.assertEqual(dll.head.next.data, 2)
        self.assertEqual(dll.head.prev, None)
        self.assertEqual(dll.count, 3)

    def test_pop_tail_when_tail_is_none(self):
        dll = doublylinkedlist.LinkedList()
        self.assertRaises(Exception, dll.pop_tail)

    def test_pop_tail_when_tail_is_one_node(self):
        dll = doublylinkedlist.LinkedList()
        dll.add(1)
        self.assertEqual(dll.tail, dll.head)
        self.assertEqual(dll.pop_tail(), 1)
        self.assertEqual(dll.tail, None)
        self.assertEqual(dll.count, 0)

    def test_pop_tail_when_tail_is_more_than_one_node(self):
        dll = doublylinkedlist.LinkedList()
        dll.add(1)
        dll.add(2)
        dll.add(3)
        dll.add(4)
        self.assertEqual(dll.pop_tail(), 1)
        self.assertEqual(dll.tail.data, 2)
        self.assertEqual(dll.tail.next, None)
        self.assertEqual(dll.tail.prev.data, 3)
        self.assertEqual(dll.count, 3)

    def test_remove_node_when_there_are_no_nodes(self):
        dll = doublylinkedlist.LinkedList()
        self.assertRaises(Exception, dll.remove_node, dll.head)

    def test_remove_node_when_head_is_tail(self):
        dll = doublylinkedlist.LinkedList()
        dll.add(1)
        dll.remove_node(dll.head)
        self.assertEqual(dll.head, None)
        self.assertEqual(dll.count, 0)

    def test_remove_node_when_there_are_many_nodes(self):
        dll = doublylinkedlist.LinkedList()
        dll.add(1)
        dll.add(2)
        dll.add(3)
        dll.add(4)
        dll.add(5)
        dll.add(6)
        dll.add(7)
        dll.remove_node(dll.head.next.next.next)
        self.assertEqual(dll.head.next.next.next.data, 3)
        self.assertEqual(dll.tail.prev.prev.prev.data, 5)
        self.assertEqual(dll.count, 6)

    def test_remove_node_when_there_are_two_nodes(self):
        dll = doublylinkedlist.LinkedList()
        dll.add(1)
        dll.add(2)
        dll.remove_node(dll.head.next)
        self.assertEqual(dll.head.next, None)
        self.assertEqual(dll.head, dll.tail)
        self.assertEqual(dll.tail.data, 2)
        self.assertEqual(dll.head.data, 2)

if __name__ == '__main__':
    unittest.main()
