'''
- Link to Problem: https://leetcode.com/problems/champagne-tower/
- Time Complexity: O(query_row^2)
- Space Complexity: O(query_row)
'''

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        currRow = [poured]

        for i in range(query_row + 1):
            nextRow = [0]*(len(currRow)+1)

            for j in range(len(currRow)):
                if currRow[j] < 1:
                    continue
                overflowed = (currRow[j] - 1) / 2
                nextRow[j] += overflowed
                nextRow[j + 1] += overflowed
                currRow[j] = 1
            if (i != query_row): currRow = nextRow[:]
        
        return currRow[query_glass]