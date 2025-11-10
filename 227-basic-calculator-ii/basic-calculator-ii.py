class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0          # current number being built
        sign = '+'       # operator BEFORE this number

        for i, ch in enumerate(s):
            if ch.isdigit():
                # build multi-digit numbers: "123" → 1 → 12 → 123
                num = num * 10 + int(ch)

            # if ch is an operator (not digit/space), or we're at the last char,
            # we "finish" the current num using the PREVIOUS sign
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    prev = stack.pop()
                    stack.append(prev * num)
                elif sign == '/':
                    prev = stack.pop()
                    # truncate toward 0 as LeetCode wants
                    stack.append(int(prev / num))

                # now this ch becomes the sign for the NEXT number
                sign = ch
                num = 0

        return sum(stack)