class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def comb(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(nums):
                return
            
            cur.append(nums[i])
            comb(i, cur, total + nums[i])
            cur.pop()

            comb(i+1, cur, total)
        
        comb(0, [], 0)
        return res
        