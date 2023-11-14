'''
- Link to Problem: https://www.geeksforgeeks.org/problems/second-largest3735/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def print2largest(self, arr: List[int], n: int) -> int:
        first, second = arr[0], -1
        for x in arr[1:]:
            if first < x:
                second = first
                first = x
            elif second < x < first:
                second = x

        return second