class Solution:
    def calculate(self, s: str) -> int:
        

        s += '+'
        num = 0 
        prev_opr = '+'
        stack = []

        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)

            elif i == ' ':
                continue
            else:
                if prev_opr == "+":
                    stack.append(num)
                elif prev_opr == "-":
                    stack.append(-num)
                elif prev_opr == "*":
                    prev_num = stack.pop()
                    stack.append(prev_num * num)
                elif prev_opr == "/":
                    prev_num = stack.pop()
                    stack.append(trunc(prev_num / num))

                num = 0
                prev_opr = i

        return sum(stack)