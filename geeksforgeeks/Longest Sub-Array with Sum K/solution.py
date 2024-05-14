'''
- Link to Problem: https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
- Time Complexity: O(N * LogN)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def lenOfLongSubarr (self, nums: List[int], n: int, k: int): 
        prefix_sum_index = {0: -1}
        ans = 0
        prefix_sum = 0
        
        for index, num in enumerate(nums):
            prefix_sum += num
            target = prefix_sum - k
            
            if target in prefix_sum_index:
                ans = max(ans, index - prefix_sum_index[target])
            
            if prefix_sum not in prefix_sum_index:
                prefix_sum_index[prefix_sum] = index
        
        return ans
