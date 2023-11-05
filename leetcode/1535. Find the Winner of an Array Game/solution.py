'''
- Link to Problem: https://leetcode.com/problems/find-the-winner-of-an-array-game/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        wins = 0
        winner = arr[0]

        for i in range(1, len(arr)):
            if winner < arr[i]:
                winner = arr[i]
                wins = 0
            wins += 1
            if wins == k: return winner

        return winner