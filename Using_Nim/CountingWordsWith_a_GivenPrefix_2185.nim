proc prefixCount(words: seq[string], pref: string): int=
    result = 0
    for w in words:
        if w[0..len(pref)-1]==pref: result+=1

# Test
echo prefixCount(@["leetcode","win","loops","success"],"")