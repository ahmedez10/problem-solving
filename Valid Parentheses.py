class Solution(object):
    def isValid(self, s):
        stack = []
        opentoclose = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in opentoclose:
                if stack and stack[-1] == opentoclose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack
