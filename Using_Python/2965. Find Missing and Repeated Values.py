from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res:List[int] = [0]*2
        counts:dict = dict().fromkeys(range(1,len(grid)*len(grid[0])+1) , 0)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                counts[grid[i][j]] += 1 
        for k,v in counts.items():
            if v==2: res[0] = k
            elif v==0: res[1] = k
        return res