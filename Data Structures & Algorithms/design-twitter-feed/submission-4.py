class Tweet:
    def __init__(self, userId, tweetId):
        self.userId = userId
        self.tweetId = tweetId
 
class Twitter:

    def __init__(self):
        """
        Notes:
        Follow/Feed Architecture:
        - Map for followers? { userId: {followeeId1, followeeId2} } (Use Set, not list)
        - Another map for followees?
        - User must be following themself to see news feed tweets - put in map 
            - They "can't" follow themself, so just restrict in follow()
        - Unfollow: Remove from userId's set

        Users:
        - User must be following themself to see news feed tweets - put in map 
        - Do they exist already, outside this class?? How to instantiate them?
            - Just from tweets themsleves I guess
        
        Tweets:
        - How to store? 
            - Normalized with tweet ID?
                > no, don't really care about ID. care more about recency
            - Based on recency?
            - Store in multiple places?
        - How to display/return?
            - Just loop & filter out based on follower set
            - Past 10 only: just keep adding to list till you hit 10?
            - Issues with storing that many tweets...??


        Follows Map:
        { 
            1: {1, 2} 
            2: {2, 1}
        }

        Tweets: [{tweetId, userId}]
        [{1, 1}, {2, 1}, {3, 2}]

        SC: O(n + m^2) -> n = num tweets, m = num users
        """
        self.tweets = []
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Publish a new tweet with ID tweetId by the user userId. 
        You may assume that each tweetId is unique.

        TC: O(1)
        """
        if userId not in self.follows:
            self.follows[userId] = set()
            self.follows[userId].add(userId)
        tweet = Tweet(userId, tweetId)
        self.tweets.append(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Fetches at most the 10 most recent tweet IDs in the user's news feed. 
        Each item must be posted by users who the user is following or by the user themself. 
        Tweets IDs should be ordered from most recent to least recent.
        - chrono.l IDs?

        TC O(n) -> n = num tweets
        """
        feed = []
        for i in range(len(self.tweets) - 1, -1, -1):
            if self.tweets[i].userId in self.follows[userId]:
                feed.append(self.tweets[i].tweetId)
            if len(feed) >= 10:
                break
        return feed
 
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        The user with ID followerId follows the user with ID followeeId.
        TC O(1)
        """
        if followerId == followeeId:
            return
        if followerId not in self.follows:
            self.follows[followerId] = set()
            self.follows[followerId].add(followerId)
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        The user with ID followerId unfollows the user with ID followeeId.
        TC O(1)
        """
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

