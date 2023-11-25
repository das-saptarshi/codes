'''
- Link to Problem: https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n, rightSum, leftSum = len(nums), sum(nums), 0
        result = []

        for i in range(len(nums)):
            rightSum -= nums[i]
            absDiff = ((i * nums[i]) - leftSum) + (rightSum - (n - 1 - i) * nums[i])
            result.append(absDiff)
            leftSum += nums[i]

        return result