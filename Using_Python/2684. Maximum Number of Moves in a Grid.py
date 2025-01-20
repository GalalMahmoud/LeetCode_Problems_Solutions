from typing import List
from functools import cache

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [[0,1],[-1,1],[1,1]]
        @cache
        def dp(row, col):
            res = 0 
            for x, y in dirs:
                new_row, new_col = row+x, col+y
                if 0<=new_row<rows and new_col<cols and grid[row][col] < grid[new_row][new_col]:
                    res = max(res,1+ dp(new_row,new_col))
            return res
        return max(dp(row, 0) for row in range(rows))