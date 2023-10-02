'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/number-of-distinct-subsequences0909/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

class Solution:
    MOD = 10**9 + 7
    def distinctSubsequences(self, S):
        n = len(S)
        dp = [1] + [0]*n
        lastOccurance = [-1] * 26
        base = ord('a')

        for i in range(1, n + 1):
            charIndex = ord(S[i - 1]) - base

            dp[i] = (2 * dp[i - 1]) % Solution.MOD
            if lastOccurance[charIndex] != -1:
                dp[i] -= dp[lastOccurance[charIndex]]

            dp[i] %= Solution.MOD
            lastOccurance[charIndex] = i - 1

        return dp[n]