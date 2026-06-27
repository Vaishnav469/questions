class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = 0
        k = len(heights) - 1
        highestwater = 0
        while j < k:
            water = (k-j) * min(heights[j], heights[k])
            highestwater = max(highestwater, water)
            if heights[j] < heights[k]:
                j += 1
            elif heights[k] < heights[j]:
                k -= 1
            else:
                j += 1
                k -= 1
            
        return highestwater