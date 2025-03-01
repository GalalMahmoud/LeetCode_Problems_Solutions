import copy
from typing import Optional

class Node:
        def __init__(self, x: int=0, next: 'Node' = None, random: 'Node' = None):
            self.val = int(x)
            self.next = next
            self.random = random




class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return copy.deepcopy(head)
    

#========================================================================
# حل آخر
# Another Solution
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        memo = {None:None}
        next_= head
        while next_:
            copy = Node(next_.val)
            memo[next_] = copy
            next_ = next_.next
        next_ = head
        while next_:
            copy = memo[next_]
            copy.next = memo[next_.next]
            copy.random = memo[next_.random]
            next_ = next_.next
        return memo[head]