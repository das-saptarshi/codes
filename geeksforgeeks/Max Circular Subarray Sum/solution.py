'''
- Link to Problem: https://www.geeksforgeeks.org/problems/max-circular-subarray-sum-1587115620/1
- Time Complexity: O(N) [N = length of nums]
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def maxCircularSum(self, nums: List[int]) -> int:
        max_subarray = self.subarraySumByKadanesAlgo(nums)
        min_subarray = self.subarraySumByKadanesAlgo(nums, findMin=True)
        
        ans = max(max_subarray, sum(nums) - min_subarray)
        if ans == 0:
            return max(nums)
        
        return ans
        
    def subarraySumByKadanesAlgo(self, nums:List[int], findMin:bool = False) -> int:
        sign = -1 if findMin else 1
        total_so_far = max_so_far = 0
        
        for num in nums:
            total_so_far += num * sign
            
            if total_so_far < 0:
                total_so_far = 0
            
            max_so_far = max(max_so_far, total_so_far)
        
        return max_so_far * sign