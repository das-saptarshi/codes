# Link to Problem: https://leetcode.com/problems/word-break/
# Time Complexity: O(n**2)
# Space Complexity: O(n)

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = {}

        def solve(s):
            if not s:
                return True
            if s in dp:
                return dp[s]
            
            for i in range(len(s)):
                r = s[:i + 1]
                if r in words and solve(s[i + 1:]):
                    dp[s] = True
                    return True
            dp[s] = False
            return False

        return solve(s)