'''
- Link to Problem: https://leetcode.com/problems/insert-delete-getrandom-o1/
- Time Complexity: O(N) [N: total number of calls made to insert, remove and getRandom]
- Space Complexity: O(M) [M: maximum number of elements present in the array at a time]
'''

import random

class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        
        self.map[val] = self.size
        if len(self.list) > self.size:
            self.list[self.size] = val
        else:
            self.list.append(val)
        self.size += 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        index = self.map[val]
        self.size -= 1
        if index != self.size:
            self.list[index] = self.list[self.size]
            self.map[self.list[self.size]] = index
        
        self.map.pop(val)
        return True

    def getRandom(self) -> int:
        return self.list[random.randint(0, self.size - 1)]