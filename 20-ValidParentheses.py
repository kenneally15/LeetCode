class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        token = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for char in s:
            
            if char in token.values():
                stack.append(char)
            elif char in token.keys():
                if stack == [] or token[char] != stack.pop():
                    return False
            else:
                return False

        return stack == []
        




