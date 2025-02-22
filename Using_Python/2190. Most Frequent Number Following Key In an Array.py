from collections import defaultdict
from typing import List

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        n=len(nums)
        t=defaultdict(int)
        max_repeat = [nums[0],1]
        for i in range(n-1):
            if nums[i]==key:
                t[nums[i+1]]+=1
                if max_repeat[1]<=t[nums[i+1]]:
                    max_repeat = [nums[i+1],t[nums[i+1]]]
        return max_repeat[0]
    
# ====================================
# أفضل حل
# Best solution
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        m = {}
        for i in range(len(nums)-1):
            if nums[i] == key: 
                m[nums[i+1]] = m.get(nums[i+1], 0)+1
        resVal, resN = 0, 0
        for target in m:
            if m[target] > resN:
                resN, resVal = m[target], target
        return resVal