# does uppercase and lowercase matter? no, so we need to convert all uppercase to lowercase to compare
# check the letter from both sides to see if they are equal to each other by using pointers
# only compare alphanumerical, because space should be not included
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # Initialize left and right pointers

        while l < r:
            # Move left pointer forward until an alphanumeric char is found
            while l < r and not self.alphaNum(s[l]):
                l += 1

            # Move right pointer backward until an alphanumeric char is found
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            
            # Compare lowercase versions of both characters
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1   # Move both pointers toward the center
        return True

    #create alphaNum
    def alphaNum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or #is it uppercase?
                ord('a') <= ord(c) <= ord('z') or #is it lowercase?
                ord('0') <= ord(c) <= ord('9'))
                
               

        