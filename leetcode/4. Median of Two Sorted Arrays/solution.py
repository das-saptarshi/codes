'''
- Link to Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/
- Time Complexity: O(m + n)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > 0 and n == 0:
            return self.findMedian(nums1)
        elif m == 0 and n > 0:
            return self.findMedian(nums2)

        first = second = i = j = 0
        steps = (m + n) // 2 + 1

        for _ in range(steps):
            if i >= m:
                second, first = first, nums2[j]
                j += 1
            elif j >= n:
                second, first = first, nums1[i]
                i += 1
            elif nums1[i] <= nums2[j]:
                second, first = first, nums1[i]
                i += 1
            else:
                second, first = first, nums2[j] 
                j += 1
        
        if (m + n) % 2 == 1:
            second = first
        
        return (first + second) / 2

        
    def findMedian(self, nums):
        n = len(nums)
        if n % 2 == 1:
            return float(nums[n // 2])
        return (nums[n // 2 -1] + nums[n // 2]) / 2