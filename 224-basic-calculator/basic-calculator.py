class Solution:
    def calculate(self, s: str) -> int:
        res = 0          # result for current parentheses level
        num = 0          # current number being built
        sign = 1         # +1 for '+', -1 for '-'
        stack = []       # stack of (previous_res, previous_sign)

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch in "+-":
                res += sign * num
                num = 0
                sign = 1 if ch == '+' else -1

            elif ch == '(':
                stack.append((res, sign))
                res = 0
                sign = 1
                num = 0

            elif ch == ')':
                res += sign * num
                num = 0
                prev_res, prev_sign = stack.pop()
                res = prev_res + prev_sign * res

        return res + sign * num