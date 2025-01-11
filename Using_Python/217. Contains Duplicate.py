from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dt = {}
        for v in nums:
            if v in dt: return True
            dt[v]=1
        return False