'''
- Link to Problem: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''


from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total, n = sum(nums), len(nums)

        if total < x:
            return -1
        if total == x:
            return n

        start = 0
        operations = -1
        for i in range(n):
            total -= nums[i]
            
            while start < i and total < x:
                total += nums[start]
                start += 1
            
            if total == x:
                operations = max(operations, i - start + 1)
        if operations == -1:
            return -1
        
        return n - operations