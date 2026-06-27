class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[ord(task) - ord('A')] = count.get(ord(task) - ord('A'), 0) + 1
        
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)

        q = deque()
        time = 0

        while maxheap or q:
            time += 1

            if not maxheap:
                time = q[0][1]
            else:
                num = 1 + heapq.heappop(maxheap)
                if num:
                    q.append([num, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
            
        return time





            
        