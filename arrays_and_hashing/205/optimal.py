# You can remove the nested loop by using the "and" statement. Also you don't even need to check for length??
# Runtime: O(N)
# Spacetime: O(2N)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_hash, t_hash = {}, {}

        for i in range(len(s)):
            if s[i] in s_hash and s_hash[s[i]] != t[i]:
                return False

            if t[i] in t_hash and t_hash[t[i]] != s[i]:
                return False

            s_hash[s[i]] = t[i]
            t_hash[t[i]] = s[i]

        return True




