'''
- Link to Problem: https://leetcode.com/problems/greatest-common-divisor-traversal/
- Time Complexity:
            1. Seive creation: O(MLogLogM) [M = max value in nums array]
            2. Prime Factor To Index creation: O(NLogN) [N = length of array nums]
            3. Graph creation: O(P * K) [P = number of distinct prime factors, K = avg indices for a prime factor]
            4. DFS traversal: O(N)
- Space Complexity: O(M + N + P * K)
'''

from typing import List
from collections import defaultdict

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) < 2: return True
        
        seive = Seive(max(nums))
        graph = Graph()

        primeToIndex = defaultdict(list)

        for i, num in enumerate(nums):
            for primeFactor in seive.getPrimeFactors(num):
                primeToIndex[primeFactor].append(i)
        
        for indexes in primeToIndex.values():
            for index in range(1, len(indexes)):
                graph.connect(indexes[index - 1], indexes[index])
        
        return graph.findConnectedVertices(0) == len(nums)



class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def connect(self, vertex1: int, vertex2: int) -> None:
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
    
    def findConnectedVertices(self, vertex: int) -> int: 
        visited = {vertex: False for vertex in self.graph.keys()}

        def dfs(node: int) -> int:
            if visited.get(node, True):
                return 0
            visited[node] = True
            vertices = 1
            for neighbor in self.graph[node]:
                vertices += dfs(neighbor)
            return vertices
        
        return dfs(vertex)

class Seive:
    def __init__(self, n: int) -> None:
        self.seive = list(range(n + 1))

        for i in range(2, n + 1):
            if self.seive[i] != i:
                continue
            for j in range(2 * i, n + 1, i):
                if self.seive[j] == j:
                    self.seive[j] = i
    
    def getPrimeFactors(self, num: int) -> List[int]:
        primeFactors = set()

        while num > 1:
            primeFactors.add(self.seive[num])
            num //= self.seive[num]
        
        return list(primeFactors)