class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create a hashset by converting the list
        numSet = set(nums)
        longest = 0
        #identify the first number in the sequence
        for n in nums:
            if (n - 1) not in numSet:
                length = 1
                #look for the future sequence numbers in the hashset
                while (n + length) in numSet:
                    length += 1
                #keep track of the current longest length
                longest = max(length, longest)

        return longest


