'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1
- Time Complexity: O(n*sum)
- Space Complexity: O(sum)
'''

class Solution:
    def perfectSum(self, arr, n, sum):
        MOD = 10**9 + 7
        dp = [1] + [0]*sum
        temp = [0]*(sum + 1)

        for i in range(n):
            for j in range(0, sum + 1):
                if arr[i] <= j:
                    p[j] = (dp[j] + dp[j - arr[i]]) % MOD
                else:
                    temp[j] = dp[j]
            dp, temp = temp, dp

        return dp[-1]