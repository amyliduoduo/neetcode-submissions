class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap to store the frequency of each character
        #key: frequency of each character for a certain group
        #value: any strings that fall into that group
        freqMap = defaultdict(list)

        
        #using a through z
        for word in strs:
            letterIndex = [0] * 26
            for letter in word:
                letterIndex[ord(letter) - ord("a")] += 1
        
            key = tuple(letterIndex)
            freqMap[key].append(word)
    

        return list(freqMap.values())
        

        #act - 0 1 2 3 4 5...
        #      1   1    
        #freqMap[key].append[n]
        #return result list