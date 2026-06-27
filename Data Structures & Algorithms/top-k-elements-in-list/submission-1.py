class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
           hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        freq = [[] for i in range(len(nums) + 1)]
        for i, j in hashmap.items():
            freq[j].append(i)

        array = []
        for i in range(len(freq) - 1, 0, -1):
            for j in range(len(freq[i])):
                array.append(freq[i][j])
                if len(array) == k:
                    return array
        
        
        
        return array