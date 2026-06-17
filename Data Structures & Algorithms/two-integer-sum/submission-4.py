class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #wanna find complement = target - num
        #hashmap to store the value/element in the list
        seen = {}

        #we need to return index at the end, so index is important
        #thats why we are using "for i..."" instead of "for n in nums"
        for i in range(len(nums)):
            complement = target - nums[i]
        
            if complement in seen:
                return [seen[complement], i]
            
            #if not found, store the current number and its index for later
            #.add is only for Sets, but here seen is a hashmap
            seen[nums[i]] = i
        