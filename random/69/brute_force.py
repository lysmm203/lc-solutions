# Brute force approach by testing every possible number
# Runtime: O(N)
# Spacetime: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x <= 3:
            return 1

        res = 2

        while res * res <= x:
            if res * res == x:
                return res
            res += 1

        return res - 1