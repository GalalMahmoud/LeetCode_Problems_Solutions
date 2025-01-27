from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        elif numRows == 2: return [[1],[1,1]]
        res=[[1],[1,1]]
        for i in range(2,numRows):
            res.append(res[-1].copy())
            res[-1].append(0)
            res[-1].insert(0,0)
            new=[]
            for j in range(1,len(res[-1])):
                new.append(res[-1][j-1]+res[-1][j])
            res[-1]=new
        return res