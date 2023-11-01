'''
- Link to Problem: https://leetcode.com/problems/flatten-nested-list-iterator/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''


from typing import List

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> List['NestedInteger']:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.flattenedList = self.flatten(nestedList)
        self.index = 0

    def flatten(self, nestedList: List[NestedInteger]) -> List[int]:
        flattenedList = []

        for element in nestedList:
            if element.isInteger():
                flattenedList.append(element.getInteger())
            else:
                flattenedList.extend(self.flatten(element.getList()))
        
        return flattenedList

    
    def next(self) -> int:
        value = self.flattenedList[self.index]
        self.index += 1
        return value
    
    def hasNext(self) -> bool:
        return self.index < len(self.flattenedList)