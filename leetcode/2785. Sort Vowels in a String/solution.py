'''
- Link to Problem: https://leetcode.com/problems/sort-vowels-in-a-string/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {x: 0 for x in 'AEIOUaeiou'}

        for x in s:
            if x in vowels:
                vowels[x] += 1
        
        result = list(s)
        index = 0

        for vowel, freq in vowels.items():
            while freq > 0:
                if result[index] in vowels:
                    result[index] = vowel
                    freq -= 1
                index += 1
        
        return ''.join(result)

'''
Note:
    This solution works without any sorting in python version 3.7 and above as the default
    dict maintains insertion order.
'''