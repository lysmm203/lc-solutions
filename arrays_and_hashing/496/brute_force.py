# Brute force solution that combs through all possible combinations
# Runtime: O(N * M)
# Spacetime: O(1), assuming the res array isn't counted as part of the spacetime complexity

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    while j < len(nums2) and nums2[j] <= nums1[i]:
                        j += 1
                    if j >= len(nums2):
                        res.append(-1)
                    else:
                        res.append(nums2[j])
                    break
        return res



