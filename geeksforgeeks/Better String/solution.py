'''
- Link to Problem: https://www.geeksforgeeks.org/problems/better-string/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def betterString(self, str1: str, str2: str) -> str:
        uniqueSubstrings1 = self.numberOfSubstrings(str1)
        uniqueSubstrings2 = self.numberOfSubstrings(str2)
        
        if uniqueSubstrings1 < uniqueSubstrings2:
            return str2
        return str1
    
    def numberOfSubstrings(self, s: str) -> int:
        map_ = {x: -1 for x in s}
        allCount = levelCount = 1
        map_[s[0]] = 1
        
        for i in range(1, len(s)):
            
            levelCount = allCount + 1
            
            if map_[s[i]] < 0:
                allCount += levelCount
            else:
                allCount += levelCount - map_[s[i]]
        
            map_[s[i]] = levelCount
        
        return allCount