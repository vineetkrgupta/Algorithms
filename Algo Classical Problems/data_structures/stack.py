"""
Stack data structure is optimized for quick appends (push) and removal of the last
node (pop)
"""

class Node:
    """Node is a simple data structure holding information"""

    def __init__(self, value, node):
        self.__value = value
        self.__next = node

    @property
    def value(self):
        """Returns the stored value"""
        return self.__value
 
    @property
    def next(self):
        """Returns the next node"""
        return self.__next

    def set_next(self, node):
        """Set the node to next"""
        if isinstance(node, Node):
            self.__next = node
        else:
            raise Exception("Not a node instance")

def create_node(value, next_node):
    """Factory function to create a node with value & next"""
    return Node(value, next_node)

class Stack:
    """Datastructure for LIFO"""

    def __init__(self):
        self.__size = 0
        self.__head = None

    def __len__(self):
        return self.__size

    def __str__(self):
        values = []
        curr_node = self.__head
        while isinstance(curr_node, Node):
            values.append(str(curr_node.value))
            curr_node = curr_node.next
        return "->".join(values)

    def push(self, value):
        """Push the value on to the stack"""
        new_node = create_node(value, self.__head)
        self.__head = new_node
        self.__size += 1

    def pop(self):
        """Remove the value from the top"""
        if self.__head is None:
            return None
        else:
            value = self.__head.value
            self.__head = self.__head.next
            self.__size -= 1
            return value

def create_stack():
    """Factory function to create a stack"""
    return Stack()

def test_simple_stack():
    """Simple visual test for stack"""
    stack = create_stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack)

if __name__ == "__main__":
    test_simple_stack()
    
