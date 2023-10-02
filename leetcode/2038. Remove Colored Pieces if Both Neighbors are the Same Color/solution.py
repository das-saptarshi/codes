'''
- Link to Problem: https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        colors += ' '
        scores = {'A': 0, 'B': 0}
        score = 1
        for i in range(1, len(colors)):
            if colors[i-1] == colors[i]:
                score += 1
            else:
                x = colors[i - 1]
                scores[x] += max(0, score - 2)
                score = 1

        return scores['A'] > scores['B']