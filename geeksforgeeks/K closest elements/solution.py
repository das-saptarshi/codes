'''
- Link to Problem: https://www.geeksforgeeks.org/problems/k-closest-elements3619/1
- Time Complexity: O(K * Log(N))
- Space Complexity: O(K)
'''

import heapq

class Solution:
    def printKClosest(self, nums, n, k, x):
        
        queue = []
        
        for num in nums:
            if x == num: continue
            heapq.heappush(queue, (-abs(x - num), num))
            
            if len(queue) > k:
                heapq.heappop(queue)
        
        return [heapq.heappop(queue)[1] for _ in range(len(queue))][::-1]