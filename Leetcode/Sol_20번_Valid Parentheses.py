class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if stack:
                if i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)

        return len(stack) == 0