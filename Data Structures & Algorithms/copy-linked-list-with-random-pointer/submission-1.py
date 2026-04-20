"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        current = head
        while current:
            new = Node(current.val)
            old_to_new[current] = new
            current = current.next

        current = head
        while current:
            old_to_new[current].next = old_to_new.get(current.next, None)
            old_to_new[current].random = old_to_new.get(current.random, None)
            current = current.next

        return old_to_new[head]