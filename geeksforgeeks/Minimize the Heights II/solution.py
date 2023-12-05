'''
- Link to Problem: https://www.geeksforgeeks.org/problems/minimize-the-heights3351/1
- Time Complexity: O(NLogN)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def getMinDiff(self, arr: List[int], n: int, k: int) -> int:
        arr.sort()
        ans = arr[n-1] - arr[0]
        
        for i in range(1, n):
            maxH = max(arr[n-1]-k, arr[i-1]+k)
            minH = min(arr[0]+k, arr[i]-k)
            
            if minH >= 0: ans = min(ans, maxH - minH)
        
        return ans