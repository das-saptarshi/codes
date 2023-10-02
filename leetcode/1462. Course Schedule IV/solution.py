'''
- Link to Problem: https://leetcode.com/problems/course-schedule-iv/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List
from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        allPrerequisites = defaultdict(set)
        graph = defaultdict(list)
        inDegree = [0]*numCourses

        for x, y in prerequisites:
            inDegree[y] += 1
            graph[x].append(y)

        queue = [x for x in range(numCourses) if inDegree[x] == 0]

        while queue:
            x = queue.pop(0)
            
            for neighbor in graph[x]:
                inDegree[neighbor] -= 1
                allPrerequisites[neighbor].update(allPrerequisites[x])
                allPrerequisites[neighbor].add(x)

                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return [x in allPrerequisites[y] for x, y in queries]