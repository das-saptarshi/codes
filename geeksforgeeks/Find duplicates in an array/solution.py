'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

class Solution:
    def duplicates(self, arr, n): 
        freq = [0]*n
        
        for x in arr:
            freq[x] += 1
        
        result = [i for i in range(n) if freq[i] > 1]
        if not result:
            return [-1]
        return result