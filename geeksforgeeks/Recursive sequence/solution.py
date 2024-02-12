'''
- Link to Problem: https://www.geeksforgeeks.org/problems/recursive-sequence1611/1
- Time Complexity: O(N^2)
- Space Complexity: O(1)
'''

class Solution:
    def sequence(self, n):
        ans = 0
        MOD = 10 ** 9 + 7
        for turn in range(1, n + 1):
            factorial = 1
            limit = turn * (turn + 1) // 2
            for i in range(turn):
                
                factorial = (factorial * (limit - i)) % MOD
            
            ans = (ans + factorial) % MOD
        
        return ans