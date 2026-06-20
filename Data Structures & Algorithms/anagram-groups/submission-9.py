class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key - group
        #key would be frequency of each character

        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
            key = tuple(count)
            groups[key].append(s)
        return list(groups.values())