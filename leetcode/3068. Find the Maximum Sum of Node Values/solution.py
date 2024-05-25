'''
- Link to Problem: https://leetcode.com/problems/find-the-maximum-sum-of-node-values/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total = count = 0
        positive = float('inf')
        negative = float('-inf')

        for num in nums:
            total += num
            change = (num ^ k) - num

            if change > 0:
                positive = min(positive, change)
                total += change
                count += 1
            else:
                negative = max(negative, change)
        
        if count % 2 == 0: return total

        return max(total - positive, total + negative)
