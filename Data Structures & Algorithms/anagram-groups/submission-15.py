class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap
        group = defaultdict(list)
    

        #go thr each word, go thr each character of that word, update in count
        for n in strs:
            #key of the hashmap is count - freq of character
            count = [0] * 26
            for c in n:
                index = ord(c) - ord("a")
                count[index] += 1

            key = tuple(count)
            group[key].append(n)

        return list(group.values())



