'''
- Link to Problem: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
- Time Complexity: O(R * C) [R = number of rows, C = number of cols]
- Space Complexity: O(R)
'''

from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ones = [freq for freq in (row.count('1') for row in bank) if freq > 0]

        return sum(ones[i] * ones[i-1] for i in range(1, len(ones)))    