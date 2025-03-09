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
    
# =============================================
# حل آخر (ليس حلي)
# Another solution (not mine)
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        currSum = (n*n)*((n*n) +1)//2
        seen = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in seen:
                    seen.add(grid[i][j])
                    currSum -= grid[i][j]
                else:
                    dup = grid[i][j]
        return [dup, currSum]