'''
- Link to Problem: https://www.geeksforgeeks.org/problems/coin-change2448/1
- Time Complexity: O(N * Sum)
- Space Complexity: O(Sum)
'''

from typing import List

class Solution:
    def count(self, coins: List[int], N: int, Sum: int) -> int:
        noOfWays = [1] + [0] * Sum
        
        for coin in coins:
            for i in range(coin, Sum + 1):
                noOfWays[i] += noOfWays[i - coin]
        
        return noOfWays[Sum]