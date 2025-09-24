'''
- Link to Problem: https://leetcode.com/problems/fraction-to-recurring-decimal/
- Time Complexity: O(D) [D = denonimator]
- Space Complexity: O(D + logN) [D = denominator, N = numerator]
'''

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        
        fraction = []
        if (numerator < 0) ^ (denominator < 0):
            fraction.append('-')
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        fraction.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return ''.join(fraction)

        fraction.append('.')
        remainders = {}

        while remainder != 0:
            if remainder in remainders:
                fraction.insert(remainders[remainder], '(')
                fraction.append(')')
                break
            
            remainders[remainder] = len(fraction)
            remainder *= 10
            fraction.append(str(remainder // denominator))
            remainder %= denominator
        
        return ''.join(fraction)