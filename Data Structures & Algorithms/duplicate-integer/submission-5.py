class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set() #initialize a hashset to store

        for n in nums:
            if n in hashset:
                return True #means duplicate
            hashset.add(n) #if no appearing in hashset, we add it to the set
        return False
