class Tweet:
    def __init__(self, userId, tweetId, timestamp):
        self.userId = userId
        self.tweetId = tweetId
        self.timestamp = timestamp
 
class Twitter:
    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.follows:
            self.follows[userId] = set()
            self.follows[userId].add(userId)
            self.tweets[userId] = []

        tweet = Tweet(userId, tweetId, self.time)
        self.tweets[userId].append(tweet)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Later timestamp first - max heap
        Tweets: {
            user1: [post1, post4]
                             p0
            user2: [post2, post5]
                             p1
            user2: [post3, post6]
                      p2
        }
        Pointers: {
            user1: 1
            user2: 1
            user3: 0
        }
        heap((post4, user1), (post5, user2), (post6, user3))

        res = []
        while heap and len(res) <= 10:
            # Find the latest from the heap
            # Add to res
            # Decremeent the chosen pointer in pointer map
            # If pointer >= 0, add it with older post to heap
        """
        # Initialize pointers
        postPointers = {}
        latestPostsHeap = []
        for followedId in self.follows[userId]:
            # Set pointer for userId to last idx of their tweet list
            postPointers[followedId] = len(self.tweets[followedId]) - 1
            # Set the userId's latest post on the heap (if any exist)
            if postPointers[followedId] >= 0:
                post = self.tweets[followedId][postPointers[followedId]]
                latestPostsHeap.append((post.timestamp, post.userId, post.tweetId))

        heapq.heapify_max(latestPostsHeap)
        tweets = []
        while latestPostsHeap and len(tweets) < 10:
            # Get the latest post from the heap
            timestamp, userId, tweetId = heapq.heappop_max(latestPostsHeap)
            # Add the tweet to the result list
            tweets.append(tweetId)
            # Decrement the tweet pointer for userId
            postPointers[userId] -= 1
            # If the user still has posts, add the next one to the heap
            if postPointers[userId] >= 0:
                nextPost = self.tweets[userId][postPointers[userId]] 
                heapq.heappush_max(
                    latestPostsHeap, 
                    (nextPost.timestamp, nextPost.userId, nextPost.tweetId))

        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.follows:
            self.follows[followerId] = set()
            self.follows[followerId].add(followerId)
            self.tweets[followerId] = []

        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

