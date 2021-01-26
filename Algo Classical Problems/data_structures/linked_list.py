"""Implementation of a linked list
watch https://www.youtube.com/watch?v=njTh_OwMljA

TODO:
1. Use Iterator patterns to loop through the linked list
    - Raise an exception when loop exists (Important)
"""

class Node:
    """Node holds a value and pointer to next node"""

    def __init__(self, value, next_node):
        """Value can be anything - str, char, number etc.
        Next node can be instance of a node or Null"""
        self.__value = value
        self.__next = next_node

    @property
    def next(self):
        """Returns the next node"""
        return self.__next

    @property
    def value(self):
        """Returns the value of the current node"""
        return self.__value

    def set_next(self, node):
        """Set the next node"""
        self.__next = node

def create_node(value, next_node):
    """Factory function to create a node with a value"""
    if isinstance(next_node, Node) or next_node is None:
        return Node(value, next_node)
    else:
        raise Exception('Next node has to be instance of class Node')

class SinglyLinkedList:
    """Singly linked list maintains a pointer to the next node"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        curr_node = self.__head
        print_arr = ['head']
        while curr_node != None:
            print_arr.append(str(curr_node.value))
            curr_node = curr_node.next
        print_arr.append('tail')
        return ' -> '.join(print_arr)

    def size(self):
        """TODO: Return the size of the linked list"""
        pass

    def append(self, value):
        """O(n) method as it requires us to touch all nodes in the list"""
        if self.__head is None:
            self.__head = create_node(value, None)
        else:
            curr_node = self.__head
            # loop until you reach the end
            while curr_node != None and curr_node.next != None:
                curr_node = curr_node.next
            curr_node.set_next(create_node(value, None))

    def prepend(self, value):
        """Prepend is very fast"""
        if self.__head is None:
            self.__head = create_node(value, None)
        else:
            new_node = create_node(value, self.__head)
            self.__head = new_node

    def remove_values(self, value):
        """Be careful when removing head node"""
        if self.__head is None:
            return
        else:
            # head is valid node so continue
            pass

        if self.__head.value == value:
            self.__head = self.__head.next
        else:
            curr_node = self.__head
            next_node = self.__head.next
            while next_node != None:
                if next_node.value == value:
                    curr_node.set_next(next_node.next)
                else:
                    # not the intended node
                    pass
                curr_node = next_node
                next_node = next_node.next

    def insert(self):
        """TODO: Insert at any arbitraty location"""
        pass


def create_linked_list():
    """Factory function to create a linked list"""
    return SinglyLinkedList()

def test_linked_list():
    """Simple linked list test"""
    linked_list = create_linked_list()
    linked_list.append(2)
    linked_list.prepend(1)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.remove_values(4)
    print(linked_list)


if __name__ == "__main__":
    test_linked_list()
