'''
- Link to Problem: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
- Time Complexity: O(N + NlogN)
- Space Complexity: O(N^2)
'''

from typing import List
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums) 
        rows = max(freq.values())
        result = [[] for _ in range(rows)] 

        for num, value in sorted(freq.items(), key = lambda x: -x[1]):
            for i in range(value):
                result[i].append(num)
        
        return result