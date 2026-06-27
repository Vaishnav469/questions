class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num = set(nums)
        largest = 0

        for i in num:
            if i - 1 not in num:
                lent = 1
                while (i + lent) in num:
                    lent += 1
                largest = max(lent, largest)
        return largest
        