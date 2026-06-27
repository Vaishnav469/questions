class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            max1 = heapq.heappop(stones)
            max2 = heapq.heappop(stones)
            difference = abs(max2 - max1)
            if difference != 0:
                heapq.heappush(stones, -difference)

        stones.append(0)
        return abs(stones[0])
        