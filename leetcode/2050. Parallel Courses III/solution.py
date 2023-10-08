'''
- Link to Problem: https://leetcode.com/problems/parallel-courses-iii/
- Time Complexity: O(N + E) [N: number of course, E: number of edges between the courses]
- Space Complexity: O(4N + E)
'''

from typing import List
from collections import defaultdict

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        degree = defaultdict(int)
        prevTime = [0]*n

        for prevCourse, course in relations:
            graph[prevCourse - 1].append(course - 1)
            degree[course - 1] += 1
        
        queue = [(course, time[course]) for course in range(n) if degree[course] == 0]
        
        ans = 0
        while queue:
            course, completionTime = queue.pop(0)
            if completionTime > ans: ans = completionTime

            for nextCourse in graph[course]:
                degree[nextCourse] -= 1
                prevTime[nextCourse] = max(prevTime[nextCourse], completionTime)
                if degree[nextCourse] == 0:
                    queue.append((nextCourse, prevTime[nextCourse] + time[nextCourse]))
        
        return ans