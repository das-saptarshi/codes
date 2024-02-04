'''
- Link to Problem: https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def missingNumber(self, nums, n):
        return (n * (n + 1) // 2) - sum(nums)