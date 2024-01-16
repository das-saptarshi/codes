'''
- Link to Problem: https://leetcode.com/problems/find-players-with-zero-or-one-losses/
- Time Complexity: O(NLogN)
- Space Complexity: O(N)
'''

from typing import List
from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set(winner for winner, _ in matches)
        losers = Counter(loser for _, loser in matches)

        allWinners = sorted(list(winner for winner in winners if winner not in losers))
        allLosers = sorted(list(loser for loser, losses in losers.items() if losses == 1))

        return [allWinners, allLosers]