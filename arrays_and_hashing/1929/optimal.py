class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Optimal: Not "optimal" in the sense that it is faster or more memory efficient than the brute force double loop solution, but it's a cleaner solution
        # Runtime: O(2N)
        # Space complexity: O(N)

        res = []

        for i in range(len(nums) * 2):
            res.append(nums[i % len(nums)])

        return res


