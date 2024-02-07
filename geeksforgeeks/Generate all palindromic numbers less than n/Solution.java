/*
- Link to Problem: https://www.geeksforgeeks.org/problems/generate-all-palindromic-numbers-less-than-n3251/1
- Time Complexity: O(N * K) [K = avg time taken to find the palindrome of a number]
- Space Complexity: O(1)
 */

class Solution {
    static int palindromicNumbers(int N){
        int palindromicNumbers = 0;
        
        for (int num = 1; num < N; num ++) {
            if (isPalindromicNumber(num)) palindromicNumbers += 1;
        }
        
        return palindromicNumbers;
    }
    
    static boolean isPalindromicNumber(int num) {
        int palindrome = 0;
        int temp = num;
        
        while (temp > 0) {
            palindrome = palindrome * 10 + temp % 10;
            temp /= 10;
        }
        
        return palindrome == num;
    }
}