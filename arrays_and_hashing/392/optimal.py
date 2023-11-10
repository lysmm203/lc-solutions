class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # Two pointer solution:
        # Initialize two pointers for s and t
        # Iterate through s and t. If s[s_ptr] == t[t_ptr], increment both the s pointer and the t pointer. Otherwise, just increment the t_ptr
        # If s_ptr == len(s) - 1, return True. Otherwise, return False
        # Runtime: O(t)
        # Space complexity: O(1)
        s_ptr, t_ptr = 0, 0

        while t_ptr < len(t) and s_ptr < len(s):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1

            t_ptr += 1

        return s_ptr == len(s)


