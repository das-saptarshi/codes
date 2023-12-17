'''
- Link to Problem: https://www.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def findMaxSum(self,nums, n):
        next1 = next2 = 0

        for num in nums:
            curr = max(next1, next2 + num)
            next1, next2 = curr, next1
        return next1