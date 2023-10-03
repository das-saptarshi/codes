'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/column-name-from-a-given-column-number4244/1
- Time Complexity: O(LogN)
- Space Complexity: O(1)
'''

class Solution:
    def colName (self, n):
        base = ord('A')
        ans = ''
        
        while n > 0:
            n -= 1
            ans = chr(base + n % 26) + ans
            n //= 26
        
        return ans