'''
- Link to Problem: https://leetcode.com/problems/count-nice-pairs-in-an-array/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List
from collections import Counter, defaultdict

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        nums = Counter(nums)
        pairs = defaultdict(int)

        for num, val in nums.items():
            rev = int(str(num)[::-1])
            pairs[num - rev] += val

        return sum(val * (val - 1) // 2 for val in pairs.values()) % (10**9 + 7)