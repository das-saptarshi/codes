'''
- Link to Problem: https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1
- Time Complexity: O(N) [N: length of string]
- Space Complexity: O(N)
'''

class Solution:
    def areIsomorphic(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        
        mapping = {}
        visited = set()
        
        for x, y in zip(str1, str2):
            if x in mapping:
                if mapping[x] != y:
                    return False
            elif y in visited:
                return False
            else:
                mapping[x] = y
                visited.add(y)
        return True