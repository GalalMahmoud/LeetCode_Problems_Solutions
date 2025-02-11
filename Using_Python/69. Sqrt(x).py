class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        while True:
            if i**2 > x:
                return i-1
            i+=1


# ===================================
# أفضل حل (ليس حلي) - يستخدم البحث الثنائي
# Best Solution (not mine) -> using binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2: return x
        l, r = 1, x//2
        while l<=r:
            mid = (l+r)//2
            sq = mid * mid
            if sq==x:
                return mid
            elif sq < x:
                l = mid +1
            else:
                r = mid-1
        return r