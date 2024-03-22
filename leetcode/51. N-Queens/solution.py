'''
- Link to Problem: https://leetcode.com/problems/n-queens/
- Time Complexity: O(N!)
- Space Complexity: O(N^2)
'''

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        board = [['.'] * n for _ in range(n)]
        cols, pos, neg = set(), set(), set()

        def placeQueen(row: int) -> None:
            if row == n:
                solutions.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if col in cols or (row + col) in pos or (row - col) in neg:
                    continue
                
                cols.add(col)
                pos.add(row + col)
                neg.add(row - col)
                board[row][col] = 'Q'

                placeQueen(row + 1)

                cols.remove(col)
                pos.remove(row + col)
                neg.remove(row - col)
                board[row][col] = '.'

        placeQueen(0)
        return solutions