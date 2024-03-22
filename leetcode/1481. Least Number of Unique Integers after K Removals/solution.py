'''
- Link to Problem: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
- Time Complexity: O(NLogN)
- Space Complexity: O(P) [P = number of unique numbers]
'''

from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        values = sorted(counter.values())

        for i in range(len(values)):
            k -= values[i]

            if k == 0:
                return len(values) - (i + 1)
            elif k < 0:
                return len(values) - i
