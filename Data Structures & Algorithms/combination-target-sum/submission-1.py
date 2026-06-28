class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.nums = nums
        self.result = []
        self.backtrack(0, 0, [])
        return self.result

    def backtrack(self, i, sumsofar, listsofar):
        if sumsofar == self.target:
            self.result.append(listsofar[:])
        elif sumsofar > self.target:
            return
        for j in range(i, len(self.nums)):
            listsofar.append(self.nums[j])
            self.backtrack(j, sumsofar+self.nums[j], listsofar)
            sumsofar-self.nums[j]
            listsofar.pop()
    
        return
        

