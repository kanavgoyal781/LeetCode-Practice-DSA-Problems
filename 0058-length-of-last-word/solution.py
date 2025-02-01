class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        k=len(s)
        if s.count(' ')==0:
            return len(s)
        while s[k-1]!=" ":
            k=k-1
        if k==0:
            return len(s)
        else:
            return len(s)-k
