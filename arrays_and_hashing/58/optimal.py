class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0

        for char in s[::-1]:
            if char == " ":
                if counter > 0:
                    break
                continue
            counter += 1

        return counter