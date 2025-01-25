from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        temp_mat=[[0]*n for _ in range(n) ]
        i=0
        j=0
        while i<n:
            j=0
            while j<n:
                temp_mat[j][n-i-1] = matrix[i][j]
                j+=1
            i+=1
        matrix[:] = temp_mat[:]