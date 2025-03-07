from typing import List
import numpy as np

# بإستخدام نامباي
# using numpy
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        try:
            return np.reshape(mat, (r,c)).tolist()
        except:
            return mat
        
# ============================================