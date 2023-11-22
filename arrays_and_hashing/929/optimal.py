# Technically optimal solution? Runs much better than the brute force code that doesn't use built-in functions.
# Runtime and spacetime complexity are still the same tho
# Runtime complexity: O(N * M)
# Spacetime complexity: O(N)

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            unique_emails.add(local + "@" + domain)

        return len(unique_emails)
