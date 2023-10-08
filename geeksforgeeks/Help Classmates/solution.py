'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/help-classmates--141631/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def help_classmate(self, arr: List[int], n: int):
        stack = []
        result = []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
            stack.append(arr[i])
        
        return result[::-1]