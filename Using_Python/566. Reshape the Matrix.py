from typing import List
import numpy as np

# بإستخدام نامباي
# Using numpy
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        try:
            return np.reshape(mat, (r,c)).tolist()
        except:
            return mat
        
# ============================================

# بدون نامباي
# Without numpy
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        grounded = []
        res:List[List[int]] = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                grounded.append(mat[i][j])

        if r * c != len(grounded): return mat
        for i in range(r):
            res.append(grounded[i*c: i*c+c])
        return res