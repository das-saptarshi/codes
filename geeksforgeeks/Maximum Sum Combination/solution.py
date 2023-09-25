'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/maximum-sum-combination/1
- Time Complexity: O(NlogN)
- Space Complexity: O(N)
'''

import heapq

class Solution:
    def maxCombinations(self, N, K, A, B):
        A.sort(reverse=True)
        B.sort(reverse=True)
        
        seen = set()
        heap = [(-A[0] - B[0], 0, 0)]
        result = []
        
        while K:
            total, i, j = heapq.heappop(heap)
            result.append(-total)
            
            if i + 1 < N and (i+1, j) not in seen:
                x, y = i + 1, j
                heapq.heappush(heap, (-A[x] - B[y], x, y))
                seen.add((x, y))
            if j + 1 < N and (i, j+1) not in seen:
                x, y = i, j + 1
                heapq.heappush(heap, (-A[x] - B[y], x, y))
                seen.add((x, y))
            K -= 1
        
        return result