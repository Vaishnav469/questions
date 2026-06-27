class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for i in nums:
            if i:
                product *= i
            else:
                zero_count += 1
        
        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            res = []
            for i in range(len(nums)):
                if nums[i] != 0:
                    res.append(0)
                else:
                    res.append(product)
            return res
        else:
            res = []
            for i in range(len(nums)):
                actual_product =  int(product / nums[i])
                res.append(actual_product)
            return res