class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        i = 0
        j = n - 1
        while i < j:
            mid = (j + i) // 2 
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] >= nums[i] and nums[mid] >= nums[j]:
                i = mid + 1
                continue
            elif nums[mid] >= nums[i] and nums[mid] <= nums[j]:
                return nums[i]
            else:
                j = mid
        return nums[i]

        

         