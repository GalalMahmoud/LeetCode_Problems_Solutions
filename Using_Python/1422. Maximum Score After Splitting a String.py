class Solution:
    def maxScore(self, s: str) -> int:
        arr=[]
        for i in range(len(s)-1):
            arr.append([])
            arr[i].append(s[:i+1])
            arr[i].append(s[i+1:])
        print(arr)
        counter=0
        current=0
        for i in range(len(arr)):
            current=0
            current+=arr[i][0].count('0')
            current+=arr[i][1].count('1')
            if current>counter: counter=current
        return counter

# =============================================
# أفضل حل (ليس حلي)
# Best solution (not mine)
class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        for i in range(len(s)):
            right += 0 if s[i]=='0' else 1;
        for i in range(len(s)-1):
            left += 1 if s[i]=='0' else 0;
            right += 0 if s[i]=='0' else -1;
            ans = max(left+right,ans)
        return ans