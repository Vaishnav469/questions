class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = []
        number = 0
        index1 = 0
        index2 = 0
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in count:
                number = difference
                index2 = i
                break
            count.append(nums[i])

        for i in range(len(nums)):
            if nums[i] == number:
                index1 = i
                break

        return [index1, index2]

