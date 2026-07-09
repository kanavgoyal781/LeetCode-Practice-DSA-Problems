class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=[]
        for i in s:
            if ('A'<=i<="Z") or ('a'<=i<='z') or ("0"<=i<="9"):
                temp.append(i.lower())
        s=''.join(c for c in temp)
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i=i+1
            j=j-1
        return True
        