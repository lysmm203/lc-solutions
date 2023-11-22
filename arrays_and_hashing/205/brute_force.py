# No idea how this solution works

# Runtime: O(N)
# Spacetime: O(2N)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_hash, t_hash = {}, {}

        for i in range(len(s)):
            if s[i] in s_hash:
                if s_hash[s[i]] != t[i]:
                    return False

            if t[i] in t_hash:
                if t_hash[t[i]] != s[i]:
                    return False

            s_hash[s[i]] = t[i]
            t_hash[t[i]] = s[i]

        if len(s_hash) != len(t_hash):
            return False

        return True




