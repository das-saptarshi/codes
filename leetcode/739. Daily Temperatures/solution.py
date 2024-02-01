'''
- Link to Problem: https://leetcode.com/problems/daily-temperatures/
- Time Complexity: O(NlogN)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if not stack:
                result[i] = 0
            else:
                result[i] = stack[-1] - i
            
            stack.append(i)
        
        return result
            