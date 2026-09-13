class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #use count array to get the frequency of 0,1,2
        count = [0] * 3
        for n in nums:
            count[n] += 1

        pointer = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[pointer] = i
                pointer += 1