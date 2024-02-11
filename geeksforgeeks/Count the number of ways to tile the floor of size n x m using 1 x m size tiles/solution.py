'''
- Link to Problem: https://www.geeksforgeeks.org/problems/count-the-number-of-ways-to-tile-the-floor-of-size-n-x-m-using-1-x-m-size-tiles0509/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

class Solution:
    def countWays(self, n, m):
        
        memo = [0] * (n + 1)
        
        for i in range(1, n + 1):
            
            if i > m:
                memo[i] = memo[i - 1] + memo[i - m]
            elif i == m:
                memo[i] = 2
            else:
                memo[i] = 1
            
        
        return memo[n] % (10 ** 9 + 7)