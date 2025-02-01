from typing import List
# الحل الأول
# Solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i!=j and target == nums[i]+nums[j]:
                    res.append(i)
                    res.append(j)
                    return res
                
################################################################
# أفضل حل
# Best solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subs = {}
        for i,n in enumerate(nums):
            if n in subs.keys():
                return [i, subs[n]]
            subs[target-n] = i
            