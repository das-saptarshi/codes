'''
- Link to Problem: https://leetcode.com/problems/valid-palindrome/
- Time Complexity: O(S) [S = length of string]
- Space Complexity: O(1)
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(x for x in s.lower() if x.isalnum())
        return s == s[::-1]
            