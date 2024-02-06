'''
- Link to Problem: https://leetcode.com/problems/group-anagrams/
- Time Complexity: O(N * (KLogK)) [N = number of words, K = avg word length]
- Space Complexity: O(1)
'''

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)
        
        return list(groups.values())