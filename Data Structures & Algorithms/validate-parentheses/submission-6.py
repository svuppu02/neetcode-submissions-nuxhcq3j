class Solution:
    def isValid(self, s: str) -> bool:
        para_dict = {")":"(", "]":"[", "}":"{"}
        stack = []
        
        for i in s:
            if i in para_dict.keys():
                print(para_dict.keys())
                if stack and stack[-1] == para_dict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False
