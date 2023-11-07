class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Brute force: Double for loop
            # Runtime: O(2N)
            # Space complexity: O(N)

        res = []

        for elem in nums:
            res.append(elem)

        for elem in nums:
            res.append(elem)

        return res