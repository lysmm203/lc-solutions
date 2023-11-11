# This solution is similar in runtime to the optimized solution, but it's just that I keep track of lastWord, which
# is an unneeded variable. Also, there is a shorter way to iterate through the string in reverse: [::-1]

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Initialize a counter variable and a lastWord variable as False
        # Iterate the string from reverse:
        # If it is a whitespace and lastWord is false, continue
        # If it is a character:
        # Set lastWord to True
        # Increment counter by 1
        # If it is a whitespace and lastWord is true:
        # break
        # return counter

        counter = 0
        lastWord = False

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and not lastWord:
                continue

            if s[i] != ' ':
                lastWord = True
                counter += 1
                print(s[i])

            if s[i] == ' ' and lastWord:
                break

        return counter
