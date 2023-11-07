class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute force: nested for loop
            # Runtime: O(n^2)
            # Space complexity: O(1)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False

        # Hashmap: trade space for time complexity
            # Runtime: O(n)
            # Space complexity: O(n) if no duplicates



