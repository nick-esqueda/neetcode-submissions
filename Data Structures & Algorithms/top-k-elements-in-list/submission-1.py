from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # SOLUTION:
        # - Iterate through nums, make count map
        # - Sort the map by values (need to flatten map into array of entries)
        # - Return a slice of the list from 0 to k

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        countList = list(counts.items())
        countList.sort(key=lambda item: item[1], reverse=True)

        result = [k for (k, v) in countList]

        return result[:k]