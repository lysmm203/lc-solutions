# Use a prefix array to cache the possible solutions. To get the sum between left and right, you just need to get the value at the right
# pointer (which is the sum of all the values from the first index to the right) and subtract it by the value at left - 1 (which would 
# be the sum of all the values before the left to right window)

# Additionally, in the for loop that initializes the prefix_arr, you don't need to consider whether i == 0 for each for loop or calculate 
# the element to append everytime if you save it in a variable curr. In the first loop, the curr will be 0. Since you will just append 
# the first element to the array, you add the first element of nums to curr and append it to prefix_arr. Now, cur holds the previous 
# value from the current iteration and you just need to add the current element and append it until the loop is over 

# Runtime: O(N)
# Spacetime: O(N)

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_arr = []
        cur = 0 
        for elem in nums:
            cur += elem
            self.prefix_arr.append(cur)
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_arr[right]

        sum_ = self.prefix_arr[right]
        return sum_ - self.prefix_arr[left-1]
        