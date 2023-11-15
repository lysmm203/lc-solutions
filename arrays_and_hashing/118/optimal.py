class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # If numRows == 1, return [[1]]
        # If numRows == 2, return [[1], [1,1]]
        # Initialize res = [[1], [1,1]]
        # Initialize a for loop with index i that loops numRows - 2 times
            # For each loop, initialize two pointers j,k with values 0 and 1. Additionally, initialize an array new_entry [1]
            # While k < len(res[i - 1]):
                # add res[i - 1][j] and res[i - 1][k]
                # Append to new_entry
                # Increment k and j by 1

            # Append 1 to new_entry
            # Append new_entry to res

        # Runtime: O(N^2)
        # Space complexity: O(N^2)

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]
        for i in range(numRows - 2):
            j, k = 0, 1
            new_entry = [1]
            prev_array = res[len(res) - 1]
            while k < len(prev_array):
                sum = prev_array[j] + prev_array[k]
                new_entry.append(sum)
                j += 1
                k += 1

            new_entry.append(1)
            print(f"Appending array: {new_entry}")
            res.append(new_entry)
        return res