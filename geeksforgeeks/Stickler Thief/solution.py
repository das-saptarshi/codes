'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/stickler-theif-1587115621/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def FindMaxSum(self,a, n):
        prevMax = 0
        currMax = a[0]
        
        for x in a[1:]:
            currMax, prevMax = max(currMax, prevMax + x), currMax
        
        return currMax