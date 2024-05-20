'''
- Link to Problem: https://www.geeksforgeeks.org/problems/modular-exponentiation-for-large-numbers5537/1
- Time Complexity: O(Log(N))
- Space Complexity: O(1)
'''

class Solution:
    def PowMod(self, x, n, m):
        if x == n == m: return 0

        def solve(x, n, m):
            ans = 1
            while n:
                if n & 1: ans = (ans * x) % m
                x = (x * x) % m
                n >>= 1
            return ans

        return solve(x, n, m)