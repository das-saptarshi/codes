# Link to Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Time Complexity: O(4^n)
# Space Complexity: O(n)

class Solution:
    keypad = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = ['']

        for digit in digits:
            chars = Solution.keypad[int(digit) - 2]

            temp = []
            for char in chars:
                for comb in result:
                    temp.append(comb + char)
            result = temp
        
        return result