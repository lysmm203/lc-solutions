# Left sum is initialize as 0 since it will be 0 for the beginning of the array. The right sum can be calculated by
# subtracting the left_sum and the current iterated element by the total sum of the array.
# Runtime: O(2N), sum operation is O(N) and the for loop is also O(N)
# Spacetime: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = sum_ - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1
