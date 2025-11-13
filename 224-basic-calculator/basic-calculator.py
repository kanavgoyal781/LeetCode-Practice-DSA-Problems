class Solution:
    def calculate(self, s: str) -> int:
        num=0
        total_result=0
        sign=1
        stack=[]
        for ind,val in enumerate(s):
            if val.isdigit():
                num=num*10+int(val)
            elif val=='+':
                total_result=total_result+num*sign
                num=0
                sign=1
            elif val=='-':
                total_result=total_result+num*sign
                num=0
                sign=-1
            elif val=='(':
                stack.append((total_result, sign))
                sign=1
                total_result=0
                num=0
            elif val==')':
                total_result += sign * num
                num=0
                prev_result,prev_sign=stack.pop()
                total_result=total_result*prev_sign+prev_result
            
        return total_result+sign*num