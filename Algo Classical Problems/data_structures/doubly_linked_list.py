"""
Doubly linked list contains pointers to prev and next
"""
import unittest


class Node(object):

    def __init__(self, value):
        self._value = value
        self._prev = None
        self._next = None


class DoublyLinkedList(object):
    """
    Implementation of a doubly linked list
    """

    def __init__(self):
        self._head = None
        self._tail = None

    def __print__(self):
        """Traverse the list"""

        curr_node = self._head

        nodes = []
        while curr_node:
            nodes.append(str(curr_node._value))
            curr_node = curr_node._next

        print("head->", end="")
        print("<->".join(nodes), end="")
        print("<-tail")

    def set_head(self, node):
        """Set the node as the head of the list"""
        if not self._head:
            self._head = node
            self._tail = node
            return

        self.insert_before(self._head, node)

    def set_tail(self, node):
        """Set the given node as tail of the list"""
        if not self._tail:
            self.set_head(node)
            return

        self.insert_after(self._tail, node)

    def insert_before(self, node, node_to_insert):
        """Method to insert before a node"""
        left_node = node._prev
        curr_node = node_to_insert
        right_node = node

        # clear the node's connections before inserting
        self.remove(node_to_insert)
        self._setup_connections(left_node, curr_node, right_node)

    def insert_after(self, node, node_to_insert):
        """Method to insert after a node"""
        left_node = node
        curr_node = node_to_insert
        right_node = node._next

        # clear the node's connections before inserting
        self.remove(node_to_insert)
        self._setup_connections(left_node, curr_node, right_node)

    def _setup_connections(self, left_node, curr_node, right_node):
        """Setup connections for nodes"""

        if left_node:
            left_node._next = curr_node
        else:
            self._head = curr_node

        curr_node._prev = left_node
        curr_node._next = right_node

        if right_node:
            right_node._prev = curr_node
        else:
            self._tail = curr_node

    def insert_at_position(self, position, node):
        """Insert the node at a given position, position starts from 1"""

        if position <= 0:
            raise ValueError("Invalid position")

        curr_node = self._head

        # special case empty list
        if not curr_node and position == 1:
            self.set_head(node)
            return

        for _ in range(1, position):
            if not curr_node:
                break

            curr_node = curr_node._next

        if curr_node:
            self.insert_before(curr_node, node)
        else:
            self.set_tail(node)

    def remove_with_value(self, value):
        """Remove all the nodes which match the given value"""

        curr_node = self._head

        while curr_node:
            next_node = curr_node._next
            if curr_node._value == value:
                self.remove(curr_node)
            curr_node = next_node

    def remove(self, node):
        """Remove the node from the list"""

        left_node = node._prev
        right_node = node._next

        # edge case: if node is head
        if self._head is node:
            self.head = right_node

        # edge case: if node is tail
        if self._tail is node:
            self._tail = left_node

        # middle
        if left_node:
            left_node._next = right_node

        if right_node:
            right_node._prev = left_node

        # reset node
        node._next = None
        node._prev = None

    def contains(self, value):
        """Check if the value exists in the list"""

        curr_node = self._head

        while curr_node:
            if curr_node._value == value:
                return True
            curr_node = curr_node._next

        return False


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = DoublyLinkedList()

    def test_set_head(self):
        node = Node(1)
        self.list.set_head(node)
        self.assertEqual(self.list._head, node)
        self.assertEqual(self.list._tail, node)
        print(self.list)

    def test_set_tail(self):
        node = Node(1)
        self.list.set_tail(node)
        self.assertEqual(self.list._head, node)
        self.assertEqual(self.list._tail, node)
        print(self.list)

    def test_insert_at(self):
        node = Node(1)
        self.list.insert_at_position(2, node)
        self.assertEqual(self.list._head, node)
        print(self.list)

    def test_insert_after(self):
        first = Node(1)
        second = Node(2)
        self.list.set_head(first)
        self.list.insert_after(first, second)

    def test_remove(self):
        node = Node(1)
        self.list.set_head(node)
        self.list.remove(node)

    def test_list_contains(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        self.list.set_head(node_1)
        self.list.insert_after(self.list._tail, node_2)
        self.list.insert_after(self.list._tail, node_3)
        self.assertTrue(self.list.contains(3))


if __name__ == "__main__":
    unittest.main()
