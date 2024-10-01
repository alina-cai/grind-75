class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                cur = stack.pop() + stack.pop()
                stack.append(cur)
            elif t == '-':
                temp = stack.pop()
                cur = stack.pop() - temp
                stack.append(cur)
            elif t == '*':
                cur = stack.pop() * stack.pop()
                stack.append(cur)
            elif t == '/':
                temp = stack.pop()
                cur = int(stack.pop() / temp)

                stack.append(cur)
            else:
                stack.append(int(t))

        return stack[0]