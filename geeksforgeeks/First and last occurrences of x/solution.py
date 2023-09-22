'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''\

class Solution:
    def find(self, arr, n, x):
        indices = [index for index, num in enumerate(arr) if num == x]
        if not indices:
            return [-1,-1]
        
        return min(indices), max(indices)