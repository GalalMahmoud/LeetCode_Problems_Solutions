from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:return head
        current = head
        holder = []
        while current:
            holder.append(current)
            if len(holder)>1 and len(holder)%k==0:
                for i in range(len(holder)//2):
                    holder[i].val,holder[-i-1].val=holder[-i-1].val,holder[i].val
                holder = []
            current = current.next
        return head