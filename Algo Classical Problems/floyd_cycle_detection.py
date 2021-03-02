"""
Cycles are notoriously dangerous bugs in linked lists. There is however a very elegant algorithm
to detect these cycles.

Edge cases:
    1. One node linked lists
    2. Loops on the first node
    3. Loop in a two node linked list
    4. Loop on the tail node
"""

def is_cycle(head):
    """Detect a cycle where a node within a linked list points to a previous node"""

    slow_runner = head
    fast_runner = head
    
    while fast_runner and fast_runner.next:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        if slow_runner is fast_runner:
            return True

    return False
