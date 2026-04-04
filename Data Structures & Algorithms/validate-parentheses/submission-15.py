class Solution:
    def isValid(self, s: str) -> bool:
        num_map = {')':'(', ']':'[', '}':'{'}

        stack = []

        for i in s:
            if i in num_map.values():
                stack.append(i)
             
            elif i in num_map.keys():
                if not stack or num_map[i] != stack.pop():
                    return False
        
        return not stack
        