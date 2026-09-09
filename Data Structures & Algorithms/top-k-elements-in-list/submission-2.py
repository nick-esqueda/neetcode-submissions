from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        SOLUTION:
        - Create a count map (1st pass) - don't yet know which one is the max right?
        - 
        - Add num to result list

        As you're iterating across for another pass, how to know which ele is the max?
        "How many does this number have"


        { 1: 1, 2: 2, 3: 3, 4: 4 }
        [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
                                
        { 1: 1, 2: 2, 3: 3, }
        maxFound = 3
        [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
                          i

        result - [4, 3]

        just iterate over the map itself k times! (instead of array)
        """

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
 
        result = list()
        maxCountFound = (0, 0) # (num, count) - num will be a neg/pos integer, count always >= 1
        for i in range(k):
            for num, count in counts.items():
                if count > maxCountFound[1]:
                    maxCountFound = (num, count)

            result.append(maxCountFound[0]) # Need to append the NUMBER, not the count
            del counts[maxCountFound[0]]
            maxCountFound = (0, 0)

        return result