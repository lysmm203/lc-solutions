# This is brute force in terms of space complexity. Apparently there's a way to do it with only O(1) space?
# Runtime: O(N)
# Spacetime: O(N)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = defaultdict(int)

        for elem in nums:
            hash[elem] += 1
            if hash[elem] > len(nums) // 2:
                return elem
