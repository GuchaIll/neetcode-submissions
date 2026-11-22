# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = 0
        power = 1
        while l1 and l2:
            res += (l1.val + l2.val) * power
            power *= 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            res += (l1.val ) * power
            l1 = l1.next
            power *= 10

        while l2:
            res += (l2.val ) * power
            l2 = l2.next
            power *= 10

        sum_node = node = ListNode()

        if res == 0:
            return ListNode(0)

        while res > 0:
            digit = res % 10
            res = res = res // 10
            node.next = ListNode(digit)
            node = node.next

        return sum_node.next

