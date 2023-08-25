# Link to Problem: https://practice.geeksforgeeks.org/problems/palindrome-string0817/1
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
	def isPalindrome(self, S):
	    return int(S == S[::-1])


# Driver Code
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)