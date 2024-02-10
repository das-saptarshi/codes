'''
- Link to Problem: https://leetcode.com/problems/palindromic-substrings/
- Time Complexity: O(N^2)
- Space Complexity: O(N^2)
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        def solve(start, end):
            nonlocal palindromes

            if start > end:
                return True

            key = (start, end)
            if key in memo:
                return memo[key]
            
            solve(start + 1, end)
            solve(start, end - 1)

            if s[start] == s[end] and solve(start + 1, end - 1):
                palindromes += 1
                memo[key] = True
            else:
                memo[key] = False

            return memo[key]
        
        palindromes = 0
        memo = {}
        solve(0, len(s) - 1)

        return palindromes