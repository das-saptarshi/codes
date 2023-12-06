'''
- Link to Problem: https://www.geeksforgeeks.org/problems/how-many-xs4514/1
- Time Complexity: O(N * K) [N: numbers between L and R, K: avg length of numbers]
- Space Complexity: O(1)
'''

class Solution:    
    def countX(self,L,R,X):
        X = str(X)
        return sum(str(x).count(X) for x in range(L + 1, R))