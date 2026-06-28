class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        i = 0
        j = n - 1
        while i < j:
            mid = (j + i) // 2 
            if nums[mid] >= nums[i] and nums[mid] >= nums[j]:
                i = mid + 1
            else:
                j = mid
        return nums[i]

        

         