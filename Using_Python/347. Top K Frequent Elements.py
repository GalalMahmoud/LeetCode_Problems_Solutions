from typing import List

# حلي يعمل و لكن ليس الأسرع
# My solution working but not the fastest 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            if i not in count: 
                count[i]=1
                continue
            count[i]+=1
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:return res
        return res
    

