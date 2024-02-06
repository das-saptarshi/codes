'''
- Link to Problem: https://leetcode.com/problems/top-k-frequent-elements/
- Time Complexity: O(NLogN)
- Space Complexity: O(N)
'''

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return sorted(freq.keys(), key = lambda x: freq[x], reverse=True)[:k]