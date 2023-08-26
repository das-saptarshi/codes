# Link to Problem: https://leetcode.com/problems/maximum-length-of-pair-chain/
# Time Complexity: O(nlogn) (sort + travelling remaining items on right for n items)
# Space Complexity: O(n) (for memoization)

from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key = lambda x: x[1])
        dp = [None]*n


        def solve(index, prev, chain):
            if index == n:
                return chain
            
            if dp[index] != None:
                return dp[index]
            
            ans = 0
            if prev < pairs[index][0]:
                ans = max(ans, solve(index + 1, pairs[index][1], chain + 1))
            ans = max(ans, solve(index + 1, prev, chain))
            dp[index] = ans

            return ans
        print(pairs)
        return solve(0, float('-inf'), 0)