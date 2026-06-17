class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            #if the left element is less than the right element, means its fully sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            #if the left side is sorted, then the minimum cannot be there, so we search the right half.
            if nums[m] >= nums[l]:
                l = m + 1
            else: 
                r = m - 1
        return res


