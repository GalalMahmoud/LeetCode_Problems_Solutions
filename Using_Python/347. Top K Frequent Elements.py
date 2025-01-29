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
    

# أسرع حل للمسألة
# Fastest solution for the problem
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        cntr = Counter(nums)
        tuple_list = []
        output = []
        for key,value in cntr.items():
            tuple_list.append((key,value))

        tuple_list.sort(key=lambda x:x[1],reverse = True)

        for key,value in tuple_list[:k]:
            output.append(key)

        return output