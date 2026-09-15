class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for bracket in s:
            if bracket in closeToOpen: #if bracket is closing
                if stack and stack[-1] == closeToOpen[bracket]:
                    stack.pop()
                else:
                    return False

            else: #if bracket is opening
                stack.append(bracket)
        
        if not stack:
            return True
        return False

