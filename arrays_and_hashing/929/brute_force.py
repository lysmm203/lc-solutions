# Brute force in that it doesn't use any of the inbuilt functions

# Runtime: O(N * M) where N is the length of emails and M is the length of the longest email string
# Space complexity: O(N)


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            local = ""
            domain = ""
            i = 0
            plus = False
            while email[i] != "@":
                if email[i] == ".":
                    i += 1
                    continue

                if email[i] == "+":
                    plus = True

                if not plus:
                    local += email[i]
                i += 1

            domain = email[i + 1:]

            unique_emails.add(local + "@" + domain)

        return len(unique_emails)