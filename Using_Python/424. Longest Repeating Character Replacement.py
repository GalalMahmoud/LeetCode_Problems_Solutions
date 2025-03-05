class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        max_freq = 0
        l = 0
        res = 0
        for i in range(len(s)):
            if s[i] not in count: count[s[i]] = 1
            else: count[s[i]] += 1
            max_freq = max(max_freq, count[s[i]])
            while (i - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, i - l +1)
        
        return res