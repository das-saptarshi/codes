'''
- Link to Problem: https://www.geeksforgeeks.org/problems/longest-subsequence-such-that-difference-between-adjacents-is-one4724/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List
from collections import defaultdict

class Solution:
    def longestSubseq(self, n : int, nums : List[int]) -> int:
        lcs = defaultdict(int)
        
        for num in nums:
            lcs[num] = max(lcs[num - 1], lcs[num + 1]) + 1
        
        return max(lcs.values())