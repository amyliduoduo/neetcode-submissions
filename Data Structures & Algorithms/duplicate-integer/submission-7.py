class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #initialize a hashset to store

        for n in nums:
            if n in seen:
                return True #means duplicate
            seen.add(n) #if no appearing in hashset, we add it to the set
        return False
