'''
- Link to Problem: https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def subArraySum(self,arr, n, s): 
        
        total = 0
        left = 0
        
        for i in range(n):
            total += arr[i]
            
            while left < i and total > s:
                total -= arr[left]
                left += 1
            
            if total == s:
                return (left + 1, i + 1)
        
        return [-1]