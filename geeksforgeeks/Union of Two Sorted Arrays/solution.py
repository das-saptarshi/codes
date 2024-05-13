'''
- Link to Problem: https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1
- Time Complexity: O(N + M)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def findUnion(self, nums1: List[int], nums2: List[int], n: int, m: int) -> List[int]:
        union = [float('-inf')]
        i = j = 0
        
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                if union[-1] != nums1[i]: union.append(nums1[i])
                i += 1
            else:
                if union[-1] != nums2[j]: union.append(nums2[j])
                j += 1
        
        while i < n:
            if nums1[i] != union[-1]: union.append(nums1[i])
            i += 1
        
        while j < m:
            if nums2[j] != union[-1]: union.append(nums2[j])
            j += 1
                
        
        return union[1:]