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