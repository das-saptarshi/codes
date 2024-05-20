'''
- Link to Problem: https://www.geeksforgeeks.org/problems/find-the-closest-number5513/1
- Time Complexity: O(Log(N))
- Space Complexity: O(1)
- Metadata:
    - Algorithm: Binary Search
'''

from typing import List

class Solution:
    def findClosest(self, n : int, k : int, nums : List[int]) -> int:
        left, right = 0, n - 1
        closet_element = nums[0]
        
        while left <= right:
            mid = (left + right) // 2
            
            if (abs(nums[mid] - k) < abs(closet_element - k) or
                (abs(nums[mid] - k) == abs(closet_element - k) and nums[mid] > closet_element)):
                    closet_element = nums[mid]
            
            if nums[mid] < k:
                left = mid + 1
            elif nums[mid] > k:
                right = mid - 1
            else:
                return nums[mid]
        
        return closet_element