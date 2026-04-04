class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paramap = {")":"(", "]":"[", "}":"{"}

        for i in s:
            if i in paramap:
                if stack and stack[-1] == paramap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False