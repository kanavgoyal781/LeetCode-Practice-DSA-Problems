class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hm={}
        hm[')']='('
        hm['}']='{'
        hm[']']='['
        for i in s:
            if i in hm.values():
                stack.append(i)
            if i in hm.keys():
                if len(stack)!=0 and hm[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack)!=0:
            return False
        else:
            return True