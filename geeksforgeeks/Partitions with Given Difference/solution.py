'''
- Link to Problem: https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1
- Time Complexity: O(S * N) [S = sum of all the elements in nums, N = total number of elements in nums]
- Space Complexity: O(S * N)
'''

from typing import List

class Solution:
    def countPartitions(self, n : int, d : int, nums : List[int]) -> int:
        
        total = sum(nums)
        
        if total < d or (total - d) % 2 != 0: return 0
        
        target = (total - d) // 2
        memo = [[0] * (target + 1) for _ in range(n + 1)]
        memo[n][0] = 1
        MOD = 10 ** 9 + 7
        
        for i in range(n - 1, -1, -1):
            for x in range(target + 1):
                withElement = memo[i + 1][x]
                wihtoutElement = 0 if x < nums[i] else memo[i + 1][x - nums[i]]
                
                memo[i][x] = (withElement + wihtoutElement) % MOD
        
        return memo[0][target]