from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next:
            next_ = head.next
            arr = []
            while next_.next:
                if next_ in arr: return True
                arr.append(next_)
                next_ = next_.next
        return False
    
# ======================================================= 
# حل أسرع
# Faster Solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next:
            next_ = head.next
            hset = set()
            while next_.next:
                if next_ in hset: return True
                hset.add(next_)
                next_ = next_.next
        return False

# ======================================================= 
# أفضل حل
# Best Solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if f == s: return True
        return False