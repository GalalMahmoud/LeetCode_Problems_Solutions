from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        stack = [head]
        next_ls = head.next
        while next_ls:
            stack.append(next_ls)
            next_ls = next_ls.next
        head=stack[-1]
        for i in range(len(stack)):
            if i == len(stack)-1: 
                stack[-i-1].next = None
                break
            stack[-i-1].next = stack[-i-2]
        return head