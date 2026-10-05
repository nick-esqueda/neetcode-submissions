class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position, speed))
        zipped.sort(key=lambda i: i[0], reverse=True)

        nextSlowest = float('-inf') # Holds the time-to-target of the slowest fleet ahead
        totalFleets = 0
        for pos, speed in zipped:
            timeToTarget = (target - pos) / speed

            if timeToTarget > nextSlowest:
                nextSlowest = timeToTarget
                totalFleets += 1
 
        return totalFleets