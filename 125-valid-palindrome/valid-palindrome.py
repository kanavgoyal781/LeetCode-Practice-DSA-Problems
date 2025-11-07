class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=[]
        for i in s:
            if ('A'<=i<="Z") or ('a'<=i<='z') or ("0"<=i<="9"):
                temp.append(i.lower())
        # s=''.join(c for c in temp) 
        left=0
        right=len(temp)-1
        while left<right:
            if temp[left]==temp[right]:
                left=left+1
                right=right-1
            else:
                return False
        return True