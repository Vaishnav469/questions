class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for i in nums:
            if i != 0:
                product *= i
            else:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            result = []
            for i in nums:
                if i != 0:
                    result.append(0)
                else:
                    result.append(int(product))
            return result
        else:
            result = []
            for i in nums:
                result.append(int(product/i))
            return result
