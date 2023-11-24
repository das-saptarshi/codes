'''
- Link to Problem: https://leetcode.com/problems/arithmetic-subarrays/
- Time Complexity: O(NLogN)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i, j in zip(l, r):
            result.append(True)
            sortedNums = sorted(nums[i: j+1])
            for k in range(len(sortedNums) - 1):
                if sortedNums[k] - sortedNums[k+1] != sortedNums[0] - sortedNums[1]:
                    result[-1] = False
                    break
            
        return result