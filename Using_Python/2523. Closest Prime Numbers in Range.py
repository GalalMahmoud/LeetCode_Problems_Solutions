from math import sqrt
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        rngl = left+1 if left%2==0 else left
        rngr = right if right%2==0 else right+1
        res = [] if left != 2 else [2]
        prev = 0    
        for i in range(rngl, rngr+1, 2):
                cnt = False
                for j in range(3,int(sqrt(i))+1,2):
                    if i%j==0: 
                        cnt = True
                        break
                if cnt: continue
                if len(res)>1:
                    if i - prev < res[-1] - res[-2]:
                        res[-1] = i
                        res[-2] = prev
                else: res.append(i)
                prev = i
        if res and res[0]==1: res[0]=2
        return res[:2] if res.__len__()>=2 else [-1,-1]