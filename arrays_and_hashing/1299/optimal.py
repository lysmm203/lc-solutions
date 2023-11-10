class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Optimal solution: Get the max value of the subset of the arrays in reverse. new[0] = max(arr[1:5]), new[1] = max(arr[2:5]). Thus, new[0] = max(arr[1], arr[2:5]) -> new[0] = max(arr[1], new[1])
            # Runtime: O(N)
            # Space complexity: O(1)

        new_max = -1 

        for i in range(len(arr) - 1, -1, -1):
            curr_val = arr[i]
            arr[i] = new_max
            new_max = max(curr_val, new_max)

        return arr 