# Solution 1:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        p = head
        while l1 and l2:
            if l1.val > l2.val:
                p.next = ListNode(l2.val)
                l2 = l2.next
            else:
                p.next = ListNode(l1.val)
                l1 = l1.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return head.next