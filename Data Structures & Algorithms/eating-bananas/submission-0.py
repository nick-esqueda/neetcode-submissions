from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        you decide K (eating speed)
        find & return the smallest K that allows you to eat all bananas within H hours

        does the remainder (%) come into account?

        starting from 1, calc how many hrs it'd take to eat all bananas (whole array)
        if hrs > H, move up and try again until you get <= H

        max possible K would be max(piles)
        H guaranteed to be >= len(piles)

        intuition: very inefficient/waste increasing speed 1 by 1 to find least. since we know low and max, binary search over all possible integer speeds (K values)

        intuition for BS optimization variation: "I don't want equals, I was the smallest possible"

        h = 9
        p = [ 1, 4, 3, 2 ]
        k = [ 1, 2, 3, 4 ]
                 l
                 r
                 k   
        k = 2 = 10hrs
        """
        def calculateHours(k):
            totalHours = 0
            for pile in piles:
                # Calculate the hours required to eat this pile at K speed
                hours = ceil(pile / k)
                # Add to running total
                totalHours += hours
            return totalHours

        l = 1
        r = max(piles)
        while l < r:
            k = (l + r) // 2
            totalHours = calculateHours(k)

            # If totalHours was within H, move R to K to try to find a smaller valid K value
            if totalHours <= h:
                r = k
            else:
                l = k + 1
        return l
 
            