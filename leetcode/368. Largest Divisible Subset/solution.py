'''
- Link to Problem: https://leetcode.com/problems/largest-divisible-subset/
- Time Complexity: O(~N^2)
- Space Complexity: O(N)
'''

from typing import Dict, List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo: Dict[int, Data] = {}

        for num in nums:
            size = 1
            parent = -1

            for key, data in memo.items():
                if num % key == 0 and (data.size + 1) > size:
                    size = data.size + 1
                    parent = key
            memo[num] = Data(size, parent)
        
        root = self.getRootOfLargestSet(memo)
        return self.getAllElementsOfSubset(root, memo)
    
    def getRootOfLargestSet(self, memo: Dict[int, 'Data']) -> int:
        size = 0
        root = None

        for key, data in memo.items():
            if data.size > size:
                size = data.size
                root = key
        
        return root

    def getAllElementsOfSubset(self, root: int, memo: Dict[int, 'Data']) -> List[int]:
        data = memo[root]

        if data.size == 1:
            return [root]
        
        return self.getAllElementsOfSubset(data.parent, memo) + [root]
    
class Data:
    def __init__(self, size: int, parent: int):
        self.size = size
        self.parent = parent