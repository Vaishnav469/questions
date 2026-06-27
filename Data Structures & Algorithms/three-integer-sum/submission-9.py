class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -n
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                    continue
                elif nums[j] + nums[k] < target:
                    j += 1
                    continue
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j < k:
                        if nums[j] == nums[j-1]:
                            j += 1
                            continue
                        if nums[k] == nums[k+1]:
                            k -= 1
                            continue
                        break
        return result