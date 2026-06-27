class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        res = 0
        for i in nums:
            if not hashmap[i]:
                hashmap[i] = hashmap[i-1] + hashmap[i+1] + 1
                hashmap[i - hashmap[i-1]] = hashmap[i]
                hashmap[i + hashmap[i+1]] = hashmap[i]
            res = max(res, hashmap[i])
 
        return res
