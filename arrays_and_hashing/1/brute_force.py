class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force solution: Nested for loop
        # Use the enumerate function of the python for loop to get both the value and the index
        # With the inner function, see if i + j = target. If so, return both the indices
        # Since there is exactly one solution, we can end the function
        # Runtime: O(N^2)
        # Space complexity: O(1)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
