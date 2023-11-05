'''
- Link to Problem: https://www.geeksforgeeks.org/problems/top-k-frequent-elements-in-array/1
- Time Complexity: O(NLogN)
- Space Complexity: O(N)
'''

from collections import Counter
from typing import List

class Solution:
	def topK(self, nums: List[int], k: int) -> List[int]:
	    return [key for value, key in sorted(((value, key) for key, value in Counter(nums).items()), reverse=True)[:k]]

