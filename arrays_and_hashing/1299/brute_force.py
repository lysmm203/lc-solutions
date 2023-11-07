class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Brute Force: Nested for loop
        # Runtime: O(N^2)
        # Space complexity: O(N)

        if len(arr) == 1:
            return [-1]

        res = []

        for i in range(len(arr) - 1):
            curr_max = 0
            for j in range(i + 1, len(arr)):
                if arr[j] > curr_max:
                    curr_max = max(curr_max, arr[j])

            res.append(curr_max)

        res.append(-1)
        return res






