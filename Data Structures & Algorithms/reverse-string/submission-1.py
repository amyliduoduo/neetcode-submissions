class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for c in s:
            stack.append(c)
        i = 0 #use pointer i to iterate thr array
        while stack:
            s[i] = stack.pop() #popping from the stack and writing each character back to s.
            i += 1