class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[l] and (nums[mid] >= target and nums[l] <= target):
               r = mid - 1
            elif nums[mid] >= nums[l] and (nums[mid] < target or nums[l] > target):
                l = mid + 1
            elif nums[mid] < nums[l] and (nums[mid] <= target and nums[r] >= target):
                l = mid + 1
            elif nums[mid] < nums[l] and (nums[mid] > target or nums[r] < target):
                r = mid - 1
            else:
                continue
        return -1