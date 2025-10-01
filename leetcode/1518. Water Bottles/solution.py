'''
- Link to Problem: https://leetcode.com/problems/water-bottles/
- Time Complexity: O(logmN) [N = number of bottles, M = exchange number]
- Space Complexity: O(1)
'''

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottlesConsumed = 0

        while numBottles >= numExchange:
            k = numBottles // numExchange
            bottlesConsumed += numExchange * k
            numBottles -= numExchange * k
            numBottles += k
        
        return bottlesConsumed + numBottles