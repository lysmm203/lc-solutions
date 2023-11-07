class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Optimal:  If these strings are of different lengths, then they cannot be an anagram. Thus, return False immediately. Afterwards, it is guaranteed that they are of the same length, and so we can stick to one loop if we make the space complexity 2N.
        # Copmaring them takes O(N) as well, however, so  runtime is O(2N)
            # Runtime: O(2N)
            # Space complexity: O(2N)

        if len(s) != len(t):
            return False

        s_hash, t_hash = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            s_hash[s[i]] += 1
            t_hash[t[i]] += 1

        return s_hash == t_hash