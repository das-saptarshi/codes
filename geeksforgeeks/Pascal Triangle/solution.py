'''
- Link to Problem: https://www.geeksforgeeks.org/problems/pascal-triangle0652/1
- Time Complexity: O(N^2)
- Space Complexity: O(N)
'''

class Solution:
    def nthRowOfPascalTriangle(self, n):
        if n == 1:
            return [1]  

        MOD = 10**9 + 7
        pascals = [1]

        for i in range(1, n + 1):
            nextRow = [1]
            for j in range(1, i - 1):
                nextRow.append((pascals[j-1] + pascals[j]) % MOD)
            nextRow.append(1)
            pascals = nextRow[:]

        return pascals