'''
- Link to Problem: https://leetcode.com/problems/distinct-subsequences/
- Time Complexity: O(S * T) [S = length of str s, T = length of str t]
- Space Complexity: O(S)
'''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        memo = [1] * (n + 1)

        for i in range(m):
            nextMemo = [0] * (n + 1)
            for j in range(n):
                nextMemo[j + 1] = nextMemo[j]

                if t[i] == s[j]:
                    nextMemo[j + 1] += memo[j]
            
            memo = nextMemo
        
        return memo[n]