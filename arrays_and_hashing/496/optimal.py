# Decreasing monotonic stack solution
# Runtime: O(N + M) where M is the length of nums1
# Spacetime: O(M) where M is the length of nums1

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash = {}
        res = [-1] * len(nums1)

        for index, elem in enumerate(nums1):
            hash[elem] = index

        for elem in nums2:
            while stack and elem > stack[-1]:
                val = stack.pop(-1)
                index = hash[val]
                res[index] = elem

            if elem in hash:
                stack.append(elem)

        return res