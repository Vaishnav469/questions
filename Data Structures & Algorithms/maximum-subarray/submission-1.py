class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub =  nums[0]
        cursum = 0
        for num in nums:
            if cursum < 0:
                cursum = 0
            cursum += num
            maxsub = max(cursum, maxsub)
        return maxsub