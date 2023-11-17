'''
- Link to Problem: https://www.geeksforgeeks.org/problems/find-the-string/1
- Time Complexity: 
- Space Complexity: 
'''

class Solution:
    def findString(self, N: int, K: int) -> str:
        unique = set()
        edges = []
        
        def solve(s: str) -> None:
            for x in range(K):
                nextS = s + str(x)
                if nextS not in unique:
                    unique.add(nextS)
                    solve(nextS[1:])
                    edges.append(str(x))
        
        solve('0'*(N - 1))
        return ''.join(edges) + '0'*(N - 1)