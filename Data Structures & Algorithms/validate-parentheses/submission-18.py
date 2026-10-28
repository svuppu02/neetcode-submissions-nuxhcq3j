class Solution:
    def isValid(self, s: str) -> bool:
        paraMap = {")":"(", "]":"[", "}":"{"}
        stack = []

        for i in s:
            if i in paraMap:
                if stack and stack[-1] == paraMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True

            

