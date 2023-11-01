'''
- Link to Problem: https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def frequencyCount(self, arr: List[int], N: int, P: int) -> None:
        
        index = 0
        
        for index in range(N):
            if arr[index] < 0:
                continue
            
            while arr[index] > 0:
                nextIndex = arr[index] - 1
                if nextIndex >= N:
                    arr[index] = 0
                    continue
                
                arr[index] = max(0, arr[nextIndex])
                
                if arr[nextIndex] > 0:
                    arr[nextIndex] = -1
                else:
                    arr[nextIndex] -= 1
                
        
        for i in range(N):
            arr[i] = abs(arr[i])