# Link to Problem: https://leetcode.com/problems/interleaving-string/
# Time Complexity: O(m*n) [where m and n are the length of the strings]
# Space Complexity: O(m*n)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        return self.solve(s1, s2, s3, len(s1)-1, len(s2)-1, len(s3)-1, set())
        

    def solve(self, s1, s2, s3, i1, i2, i3, dp):
        if i1 < 0 and i2 < 0:
            return True
        
        key = (i1, i2)
        if key in dp:
            return False
        
        if i1 >= 0 and s1[i1] == s3[i3]:
            if self.solve(s1, s2, s3, i1 - 1, i2, i3 - 1, dp):
                return True

        if i2 >= 0 and s2[i2] == s3[i3]:
            if self.solve(s1, s2, s3, i1, i2 - 1, i3 - 1, dp):
                return True

        dp.add(key)
        return False