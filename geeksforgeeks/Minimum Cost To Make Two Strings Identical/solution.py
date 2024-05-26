'''
- Link to Problem: https://www.geeksforgeeks.org/problems/minimum-cost-to-make-two-strings-identical1107/1
- Time Complexity: O(X * Y) [X = length of string x, Y = length of string y]
- Space Complexity: O(X * Y)
- Metadata:
    - Algorithm: Longest Common Subsequence
'''

class Solution:
    def findMinCost(self, x: str, y: str, costX: int, costY: int) -> int:
        dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]

        for i in range(1, len(x) + 1):
            for j in range(1, len(y) + 1):

                if x[i - 1] == y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        longest_common_subsequence_len = dp[len(x)][len(y)]

        return costX * (len(x) - longest_common_subsequence_len) + costY * (len(y) - longest_common_subsequence_len)