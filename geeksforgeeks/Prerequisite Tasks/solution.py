'''
- Link to Problem: https://www.geeksforgeeks.org/problems/prerequisite-tasks/1
- Time Complexity: O(V + E) [V = number of vertices, E = number of edges]
- Space Complexity: O(V)
'''

from typing import List

class Solution:
    def isPossible(self, N: int, P: int, prerequisites: List[List[int]]) -> bool:
        dependencies = [0] * N
        nextTasks = [[] for _ in range(N)]
        
        for task, prerequisite in prerequisites:
            nextTasks[prerequisite].append(task)
            dependencies[task] += 1
        
        queue = [task for task, dependency in enumerate(dependencies) if dependency == 0]
        
        tasksCompleted = 0
        while queue:
            task = queue.pop(0)
            tasksCompleted += 1
            for nextTask in nextTasks[task]:
                dependencies[nextTask] -= 1
                
                if dependencies[nextTask] == 0:
                    queue.append(nextTask)
        
        return tasksCompleted == N