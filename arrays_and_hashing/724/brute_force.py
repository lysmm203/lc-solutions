# While iterating through every index, just manually calculate the left and right sides, compare them, and determine
# if a pivot index exists of not. A lot of repeated calculations
# Runtime: O(N^2)
# Spacetime: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        for index in range(len(nums)):
            if index == 0:
                left_sum = 0
            else:
                left_sum = sum(nums[:index])

            right_sum = sum(nums[index + 1:])

            if left_sum == right_sum:
                return index

        return -1

