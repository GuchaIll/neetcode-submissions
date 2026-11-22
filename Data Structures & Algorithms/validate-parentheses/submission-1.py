class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        brackets = {
            ")" : "(",
            "]" : "[",
            "}" : "{" 
        }

        opened = set(brackets.values())
        for i in range(len(s)):
            if s[i] in opened:
                stack.append(s[i])
            else:
                if len(stack) == 0 or stack[-1] != brackets[s[i]]:
                    return False
                stack.pop()

        return len(stack) == 0


