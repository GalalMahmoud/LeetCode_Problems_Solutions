from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i!=j and target == nums[i]+nums[j]:
                    res.append(i)
                    res.append(j)
                    return res