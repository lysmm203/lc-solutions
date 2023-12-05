# Basic ass solution
# Runtime: O(N)
# Spacetime: O(N)

class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        for i in range(left, right + 1):
            res += self.arr[i]

        return res
