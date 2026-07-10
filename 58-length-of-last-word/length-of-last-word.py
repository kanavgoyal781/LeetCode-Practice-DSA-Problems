class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        i=len(s)-1
        j=len(s)-1
        while s[i]!=" " and i>=0:
            i=i-1
        return j-i
        