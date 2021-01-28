"""
Queue is FIFO
"""

class Node:
    """Holds value and next"""

    def __init__(self, value, node):
        self.__value = value
        self.__next = node

    @property
    def value(self):
        """Return the value"""
        return self.__value

    @property
    def next(self):
        """Return the next pointer"""
        return self.__next

    def set_next(self, node):
        """Set the next node"""
        self.__next = node

class Queue:
    """Queue implementation using linked lists"""

    def __init__(self):
        self.__size = 0
        self.__head = None
        self.__tail = None

    def __len__(self):
        return self.__size

    def __str__(self):
        values = ["head"]
        curr_node = self.__head
        while isinstance(curr_node, Node):
            values.append(str(curr_node.value))
            curr_node = curr_node.next
        values.append("tail")
        return "->".join(values)

    def enqueue(self, value):
        """Add to the end of the queue"""
        new_node = Node(value, None)

        # if list is empty
        if self.__size == 0:
            self.__head = new_node
            self.__tail = new_node
            self.__size += 1
        else:
            new_node = Node(value, None)
            self.__tail.set_next(new_node)
            self.__tail = new_node
            self.__size += 1

    def dequeue(self):
        """Remove from the beginning of the queue"""
        if self.__size == 0:
            return None
        else:
            value = self.__head.value
            self.__head = self.__head.next
            self.__size -= 1
            return value

def test_simple_queue():
    """Simple visual test for queue"""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue)

if __name__ == "__main__":
    test_simple_queue()
