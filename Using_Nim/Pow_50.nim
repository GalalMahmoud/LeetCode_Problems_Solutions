import std/math
proc myPow(x: float, n: int):float=
        return math.pow(x, float(n))

# Test
echo myPow(2,6)