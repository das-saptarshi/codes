'''
- Link to Problem: https://leetcode.com/problems/relative-ranks/
- Time Complexity: O(N * Log(N))
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        
        topTitles = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        def getPositionTitle(position):
            if position < 4:
                return topTitles[position - 1]
            
            return str(position)

        answer = [''] * len(scores)
        indices = {score: i for i, score in enumerate(scores)}
        scores.sort(reverse=True)

        for i, score in enumerate(scores):
            answer[indices[score]] = getPositionTitle(i + 1)
        
        return answer