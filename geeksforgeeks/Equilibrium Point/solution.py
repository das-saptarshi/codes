'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def equilibriumPoint(self,A, N):
        afterSum = sum(A)
        beforeSum = 0
        
        for i in range(N):
            afterSum -= A[i]
            if beforeSum == afterSum:
                return i + 1
            beforeSum += A[i]
        
        return -1