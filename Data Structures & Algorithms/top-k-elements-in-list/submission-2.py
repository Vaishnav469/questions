class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        for i in range(len(nums)):
            freqmap[nums[i]] = 1 + freqmap.get(nums[i], 0)

        maxfreq = [[] for i in range(len(nums) + 1)]
        for key, freq in freqmap.items():
            maxfreq[freq].append(key)
        result = []
        for i in range(len(maxfreq) - 1, 0, -1):
            for j in range(len(maxfreq[i])):
                result.append(maxfreq[i][j])
                if len(result) == k:
                    return result
