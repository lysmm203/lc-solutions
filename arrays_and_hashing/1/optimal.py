class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Optimal solution: Use a hashmap and loop through only once
        # Initialize a hashmap and start the for loop
        # Within the for loop, check if the target - current element is in hash. If it is, return the indices
        # Add the val and index to the hash
        # Runtime: O(N)
        # Space complexity: O(N)

        hash = {}

        for index, val in enumerate(nums):
            if target - val in hash:
                return [hash[target - val], index]
            hash[val] = index