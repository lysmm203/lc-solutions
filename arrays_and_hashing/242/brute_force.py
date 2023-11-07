class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute: Accounting for different lengths, run different loops for each input, and return True if the hash has all its elements set to 0. Otherwise, return False
        # Runtime: O(3N)
        # Space complexity: O(N)

        hash = defaultdict(int)

        for i in range(len(s)):
            hash[s[i]] += 1

        for i in range(len(t)):
            hash[t[i]] -= 1

        for key in hash:
            if hash[key] != 0:
                return False

        return True

