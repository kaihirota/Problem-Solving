"""
929. Unique Email Addresses
https://leetcode.com/problems/unique-email-addresses/
"""
from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        recipients = set()
        for email in emails:
            local, host = email.split('@')
            local = [char for char in local if char != '.']
            i = 0
            while i < len(local) and local[i] != '+':
                i += 1
            if i > 0:
                local = "".join(local[:i])
            else:
                local = "".join(local)
            address = local + '@' + host
            if address not in recipients:
                recipients.add(address)

        return len(recipients)


Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"])
