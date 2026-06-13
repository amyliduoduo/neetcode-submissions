class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #same amount of the characters
        countS = {}
        countT = {}
        
        #count the characters of string s and string t independently, and only compare them after the loops are entirely finished.
        for char in s:
            countS[char] = 1 + countS.get(char, 0)
        for char in t: 
            countT[char] = 1 + countT.get(char, 0)
        

        return countS == countT