class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for n in strs:
            count = [0] * 26
            for c in n:
                index = ord(c) - ord("a")
                count[index] += 1
            
            key = tuple(count)
            groups[key].append(n)

        return list(groups.values())