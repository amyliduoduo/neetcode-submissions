class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

       # find the pivot
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else: 
                r = m

        pivot = l

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return -1
        
        # First, search the left half
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
            
        # If not found on the left, search and return from the right half
        return binary_search(pivot, len(nums) - 1)
