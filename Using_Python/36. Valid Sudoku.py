from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dtrow = defaultdict(set)
        dtcol = defaultdict(set)
        dtquad = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col]==".":continue
                if (board[row][col] in dtrow[row] or
                    board[row][col] in dtcol[col] or
                    board[row][col] in dtquad[(row//3, col//3)]): return False

                dtrow[row].add(board[row][col])
                dtcol[col].add(board[row][col])
                dtquad[(row//3, col//3)].add(board[row][col])
        return True