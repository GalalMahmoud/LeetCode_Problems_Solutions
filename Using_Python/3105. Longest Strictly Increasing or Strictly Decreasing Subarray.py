from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = inc = decr = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: 
                inc += 1
                decr = 1
            elif nums[i]<nums[i-1]:
                decr += 1
                inc = 1
            else: 
                inc = decr = 1
            res = max(res, inc, decr)
        return res