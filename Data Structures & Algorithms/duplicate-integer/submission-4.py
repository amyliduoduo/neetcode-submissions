class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                #.add for set, .append for list
                #set only store each element once
                seen.add(n)
        return False