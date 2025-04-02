from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        next_ = head
        lnlen = 0
        while next_:
            lnlen+=1
            next_= next_.next
        next_ = head
        for i in range(lnlen-n+1):
            if lnlen!=n and i == lnlen-n-1:
                if next_.next: next_.next= next_.next.next
                else: next_.next = None
                break
            elif lnlen == n:
                head = head.next
                break
            next_ = next_.next
            
        return head