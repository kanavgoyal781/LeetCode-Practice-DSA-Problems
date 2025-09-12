class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        if len(path)==0:
            return
        i=1
        temp=''
        while i<len(path):
            if path[i]=='/':
                temp=''
                i=i+1
                continue
            while i<len(path) and path[i]!='/':
                temp=temp+path[i]
                i=i+1
            if temp!='..' and temp!='.':
                stack.append(temp)
            if stack and temp=='..':
                stack.pop()
        if not stack:
            return "/"
        else:
            return "/" + "/".join(stack)
        # return stack
