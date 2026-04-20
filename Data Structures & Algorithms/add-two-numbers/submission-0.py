# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, node_a: Optional[ListNode], node_b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1) # dummy node
        out_node = dummy
        
        carry = 0
        while node_a and node_b:
            result = node_a.val + node_b.val + carry
            out_node.next = ListNode(result % 10)
            carry = result // 10

            node_a = node_a.next
            node_b = node_b.next
            out_node = out_node.next

        while node_a:
            result = node_a.val + carry
            out_node.next = ListNode(result % 10)
            carry = result // 10

            node_a = node_a.next
            out_node = out_node.next

        while node_b:
            result = node_b.val + carry
            out_node.next = ListNode(result % 10)
            carry = result // 10

            node_b = node_b.next
            out_node = out_node.next

        while carry > 0:
            out_node.next = ListNode(carry % 10)
            out_node = out_node.next

            carry = carry // 10

        return dummy.next



