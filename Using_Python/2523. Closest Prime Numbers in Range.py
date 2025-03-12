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

# =====================================================
# أفضل حل (ليس حلي)
# Best solution (not mine)
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right - left < 1:
            return [-1, -1]

        left = max(2, left)
        if left == 2 and right >= 3:
            return [2, 3]
        
        if left & 1 == 0:
            left += 1

        prev_prime = -1
        min_diff = float('inf')
        res = [-1, -1]

        def is_composite_witness(n: int, witness: int, d: int, s: int) -> bool:
            x = pow(witness, d, n)
            if x == 1 or x == n - 1:
                return False
            for _ in range(1, s):
                x = pow(x, 2, n)
                if x == n - 1:
                    return False
            return True

        def miller_rabin(n: int) -> bool:
            if n < 2:
                return False
            small_primes = [2, 3]
            for p in small_primes:
                if n == p:
                    return True
                if n % p == 0:
                    return False

            s = 0
            d = n - 1
            while d & 1 == 0:
                d >>= 1
                s += 1

            for witness in small_primes:
                if is_composite_witness(n, witness, d, s):
                    return False
            return True

        for candidate in range(left, right + 1, 2):
            if not miller_rabin(candidate):
                continue

            if prev_prime != -1:
                diff = candidate - prev_prime
                if diff == 2:
                    return [prev_prime, candidate]
                if diff < min_diff:
                    min_diff = diff
                    res = [prev_prime, candidate]

            prev_prime = candidate

        return res