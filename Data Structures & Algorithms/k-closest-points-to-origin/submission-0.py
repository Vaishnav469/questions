class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []

        for point in points:
            distance = point[0]*point[0] + point[1]*point[1]
            if not res:
                res.append([-distance, point])
            else:
                heapq.heappush(res, [-distance, point])
                if len(res) > k:
                    heapq.heappop(res)

        for i in range(len(res)):
            res[i] = res[i][1]
        return res
            
                
            
        