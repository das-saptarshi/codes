'''
- Link to Problem: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
- Time Complexity: O(N)
- Space Complexity: O(N) [N for the Dictionary]
'''


from typing import List
from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        for i, x in enumerate(groupSizes):
            groups[x].append(i)
        
        return [group[i: i + size] for size, group in groups.items() for i in range(0, len(group), size)]
            