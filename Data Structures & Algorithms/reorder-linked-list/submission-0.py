class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find middle
        fast_pointer = head
        slow_pointer = head
        previous = None

        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            previous = slow_pointer
            slow_pointer = slow_pointer.next

        previous.next = None

        # 2. Reverse second half
        previous = None
        current = slow_pointer

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        # 3. Merge
        node_a = head
        node_b = previous

        while node_a.next and node_b.next:
            temp_a = node_a.next
            temp_b = node_b.next
            node_a.next = node_b
            node_b.next = temp_a
            node_a = temp_a
            node_b = temp_b

        node_a.next = node_b
