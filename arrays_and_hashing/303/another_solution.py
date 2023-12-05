# Attempt to reduce runtime by caching the solutions in a nested hashmap
# Runtime: O(N)
# Spacetime: O(N^2)

class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.hash = {}

    def sumRange(self, left: int, right: int) -> int:
        if left not in self.hash or right not in self.hash[left]:
            res = 0
            for i in range(left, right + 1):
                res += self.arr[i]
            self.hash[left] = {right: res}

            return res

        return self.hash[left][right]


