class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0:
            return False
        h={}
        stack=[]
        h[')']='('
        h[']']='['
        h['}']='{'
        for i in range(len(s)):
            if s[i] in h.values():
                stack.append(s[i])
            elif not stack:
                return False
            elif h[s[i]]==stack[-1]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True

        