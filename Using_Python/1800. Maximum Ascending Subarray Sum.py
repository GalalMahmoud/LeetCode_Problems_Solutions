from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        carrier = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                carrier += nums[i]
            else: carrier = nums[i]
            res = max(carrier, res)
        return res