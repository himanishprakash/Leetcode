class Solution:
    def calculate(self, s: str) -> int:

        s += '+'
        num = 0
        prev_op = '+'
        stack = []

        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
                
            elif i == ' ':
                continue
            else:
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    prev_num = stack.pop()
                    stack.append(num * prev_num)
                elif prev_op == '/':
                    prev_num = stack.pop()
                    stack.append(trunc(prev_num/ num))
                
                num = 0
                prev_op = i

        return sum(stack)
        
