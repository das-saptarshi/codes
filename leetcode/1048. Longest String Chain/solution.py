'''
- Link to Problem: https://leetcode.com/problems/longest-string-chain/
- Time Complexity: O(N*K) [N: number of words, K: Avg length of words]
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = set(words)

        def longestChain(word):
            if word not in words:
                return 0

            if word in dp:
                return dp[word]

            ans = 0
            for i in range(len(word)):
                ans = max(ans, longestChain(word[:i] + word[i+1:]))
            
            ans += 1
            dp[word] = ans
            return ans
        
        dp = {}
        result = 0
        for word in words:
            result = max(result, longestChain(word))
            
        return result
        