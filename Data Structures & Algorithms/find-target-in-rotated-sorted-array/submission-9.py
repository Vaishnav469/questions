class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[i] and nums[mid] >= target and nums[i] <= target:
                j = mid
            elif nums[mid] >= nums[i] and (nums[mid] < target or nums[i] > target):
                i = mid + 1
            elif nums[mid] <= nums[i] and nums[mid] <= target and nums[j] >= target:
                i = mid + 1
            elif  nums[mid] <= nums[i] and (nums[mid] > target or nums[j] < target):
                j = mid
            else:
                break

        
        return -1
 
