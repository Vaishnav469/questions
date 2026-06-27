class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        CurMax, CurMin = 1, 1

        for i in nums:
            if i == 0:
                CurMax, CurMin = 1, 1
                continue

            temp = CurMax
            CurMax = max(i * CurMax, i * CurMin, i)
            CurMin = min(i * temp, i * CurMin, i)
            res = max(res, CurMax)

        return res        