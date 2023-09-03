'''
- Link to Problem: https://leetcode.com/problems/unique-paths/
- Time Complexity: O(m + n)
- Space Complexity: O(1)
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        return self.factorial(m+n-2) // (self.factorial(n-1)*self.factorial(m-1))
        
    def factorial(self, num):
        ans = 1
        while num > 1:
            ans *= num
            num -= 1
        return ans
        