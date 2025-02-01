class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False
            
        # Single digit numbers are always palindromes
        if x < 10:
            return True
            
        # Convert to string and compare
        return str(x) == str(x)[::-1]
