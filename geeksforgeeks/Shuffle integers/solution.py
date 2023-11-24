'''
- Link to Problem: https://www.geeksforgeeks.org/problems/shuffle-integers2401/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def shuffleArray(self, arr: List[int], n: int):
        arr[:] = [x for pair in zip(arr[:n // 2], arr[n//2: ]) for x in pair]
