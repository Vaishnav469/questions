class Twitter:

    def __init__(self):
        self.count = 0
        self.followmap = defaultdict(set)
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []

        self.followmap[userId].add(userId)
        for followid in self.followmap[userId]:
            if followid in self.tweets:
                for i in range(len(self.tweets[followid])):
                    count, tweetId = self.tweets[followid][i]
                    heapq.heappush(minheap, [count, tweetId])
                    if len(minheap) > 10:
                        heapq.heappop(minheap)
                    
        while minheap:
            res.append(heapq.heappop(minheap)[1])
        return res[::-1]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        
