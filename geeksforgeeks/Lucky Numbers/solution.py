'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/lucky-numbers2911/1
- Time Complexity: O(logN)
- Space Complexity: O(1)
'''

class Solution:
    def isLucky(self, n): 
        x = 2
        
        while x <= n:
            if n % x == 0:
                return False
            
            n -= n // x
            x += 1
          
        return True