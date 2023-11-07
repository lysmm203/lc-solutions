class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute force: nested for loop
            # Runtime: O(n^2)
            # Space complexity: O(1)

        # Hashmap: trade space for time complexity. Use a set so you don't have to add arbitrary values to the dictionary
            # Runtime: O(n)
            # Space complexity: O(n) if no duplicates

        hash = set()

        for elem in nums:
            if elem in hash:
                return True
            hash.add(elem)

        return False



