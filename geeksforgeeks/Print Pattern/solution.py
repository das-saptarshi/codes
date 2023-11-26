'''
- Link to Problem: https://www.geeksforgeeks.org/problems/print-pattern3549/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def pattern(self, N: int) -> List[int]:
        if N <= 0:
            return [N]
        
        result = list(range(N, -1, -5))
        
        if result[-1] != 0:
            result.append(result[-1] - 5)
        
        return result + (result[:-1])[::-1]