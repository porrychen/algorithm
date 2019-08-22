"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here

        dummy = ListNode(0)
        dummy.next, slow = head, dummy

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
