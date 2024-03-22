'''
- Link to Problem: https://www.geeksforgeeks.org/problems/power-set4302/1
- Time Complexity: O(2^N)
- Space Complexity: O(2^N)
'''

class Solution:
    def AllPossibleStrings(self, s):

        def permutations(index, permutation):
            if index == n:
                return [permutation]

            return permutations(index + 1, permutation + s[index]) + permutations(index + 1, permutation)

        n = len(s)
        return sorted(permutations(0, ''))[1:]