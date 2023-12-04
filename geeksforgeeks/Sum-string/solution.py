'''
- Link to Problem: https://www.geeksforgeeks.org/problems/sum-string3151/1
- Time Complexity: O(N^3)
- Space Complexity: O(N)
'''

class Solution:
    def isSumString (self, S):
        
        def recursiveCheck(i, j, k):
            if k == len(S):
                return True
            elif k > len(S):
                return False
            
            num1 = int(S[i: j])
            num2 = int(S[j: k])
            
            num3 = str(num1 + num2)
            
            return S[k: ].startswith(num3) and recursiveCheck(j, k, k + len(num3))
        
        
        for i in range(1, len(S)):
            for j in range(i + 1, len(S)):
                if recursiveCheck(0, i, j): return 1
        
        return 0