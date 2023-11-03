'''
- Link to Problem: https://leetcode.com/problems/build-an-array-with-stack-operations/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        index, x, targetLen = 0, 1, len(target)
        operations = []

        while index < targetLen and x <= n:
            operations.append('Push')
            if target[index] != x:
                operations.append('Pop')
            else:
                index += 1
            x += 1
        
        return operations