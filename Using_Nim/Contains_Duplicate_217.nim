import tables
import std/strformat

proc containsDuplicate(nums: seq[int]): bool=
    var dt = {"":NaN}.toTable
    for v in nums:
        if hasKey(dt,fmt"{v}"): return true
        dt[fmt"{v}"] = 1
    return false

# Test
echo containsDuplicate(@[1,2,3,4,1])