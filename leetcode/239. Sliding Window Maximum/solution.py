'''
- Link to Problem: https://leetcode.com/problems/sliding-window-maximum/
- Time Complexity: O(N)
- Space Complexity: O(K)
'''

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        queue = deque([])
        ans = []

        for i in range(n):
            while queue and queue[0] < i - k + 1:
                queue.popleft()
            
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            queue.append(i)

            if i >= k - 1:
                ans.append(nums[queue[0]])
        
        return ans