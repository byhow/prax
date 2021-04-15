# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lefthead = lefthead_ptr = ListNode(0)
        righthead = righthead_ptr = ListNode(0)
        
        while head:
            if head.val < x:
                lefthead_ptr.next =head
                lefthead_ptr = lefthead_ptr.next
            else:
                righthead_ptr.next =head
                righthead_ptr = righthead_ptr.next
            
            head = head.next
        
        righthead_ptr.next = None
        
        lefthead_ptr.next = righthead.next
        return lefthead.next