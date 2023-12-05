# Binary search approach
# Runtime: O(logN)
# Spacetime: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0

        while right >= left:
            mid = (left + right) //2

            if mid * mid < x:
                left = mid + 1
                res = mid
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid

        return res