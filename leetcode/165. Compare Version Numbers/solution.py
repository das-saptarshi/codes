'''
- Link to Problem: https://leetcode.com/problems/compare-version-numbers/
- Time Complexity: O(L) [L = max length between version1 and version2]
- Space Complexity: O(L)
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version_1 = version1.split('.')
        version_2 = version2.split('.')

        def get_version_number(index, version):
            if index >= len(version):
                return 0
            
            return int(version[index])
        
        
        for i in range(max(len(version_1), len(version_2))):
            version_number_1 = get_version_number(i, version_1)
            version_number_2 = get_version_number(i, version_2)

            if version_number_1 < version_number_2: return -1
            if version_number_1 > version_number_2: return 1
        
        return 0