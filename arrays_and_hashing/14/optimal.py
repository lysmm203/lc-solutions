# I think the brute force would just be a nested for loop, but coding it seems more complicated than the more optimal
# solution so I'll just leave the optimal solution here
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        # ["flower","flow","flight"]
        # ["dog","racecar","car"]
        # ["", ""]
        # ["flower", "flow", ""]

        # Set res to the first word. Create a for loop to iterate through the array
        # For each iteration, while res != word, remove the last letter of res
        # If len(res) == 0, return res

        # return res

        # Runtime: O(N * M) where N is the length of strs and M is the length of the longest string
        # Space complexity: O(1)

        res = strs[0]

        for string in strs:
            while res != string[:len(res)]:
                if res == "":
                    return res
                res = res[:len(res) - 1]

        return res



