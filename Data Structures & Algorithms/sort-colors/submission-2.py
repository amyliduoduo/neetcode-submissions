class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Dutch National Flag
        #nums = [0...l-1 l...i-1 i...r r+1...end]

        l = 0 #boundary for 0s
        i = 0 #current element
        r = len(nums) - 1 #boundary for 2s

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0:
                swap(l, i) #place 0 to the left zone
                l += 1 #expand the 0 boundary forward
            elif nums[i] == 2:
                swap(i, r) #place 2 to the right zone
                r -= 1 #expand the 2 boundary backward
                i -= 1 #cancel out the upcoming i += 1
            #continue the next element
            i += 1



