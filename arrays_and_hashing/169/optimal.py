# Uses Boyer Moore's algorithm
# Runtime: O(N)
# Spacetime: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = None, 0

        for elem in nums:
            if count <= 0:
                res = elem

            count = count + 1 if elem == res else count - 1

        return res
