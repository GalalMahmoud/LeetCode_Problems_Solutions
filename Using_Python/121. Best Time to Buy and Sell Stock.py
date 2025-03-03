from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profite=0
        min_price = float('inf')
        for p in prices:
            profite = max(profite, p - min_price)
            min_price = min(min_price , p)
        return profite