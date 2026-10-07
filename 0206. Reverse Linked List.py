# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        
        p, head, n = head, head.next, head.next.next

        p.next = None
        
        head.next = p
        
        while n:
            p, head, n = head, n, n.next
            head.next = p
        return head
