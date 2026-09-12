class Solution:
    def isValid(self, s: str) -> bool:
        #create a hashmap to lookup the pairs of brackets
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}
        #create a stack to store opening brackets
        stack = []

        for bracket in s:
            if bracket in closeToOpen:
                if stack and stack[-1] == closeToOpen[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        if not stack:
            return True
        return False
