class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        Output: 3

        car #  0 1 2 3
        pos = [4,1,0,7]
        spd = [2,2,1,1]

        0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
        -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
                    0
           1
        2
                             3

        0 - ~8 hr to target~
        1 - ~9.5hr to target~
        2 - 19hr to target
        3 - 12hr to target
                            
 
        whatever car is slowest and farthest along will block prev ones
        - unless prev car won't catch up

        "when do you reach the finish line?"
        - if it's before a car ahead of it, then it'd add to the fleet

        if a car would reach the target before a later car would, then it wouldn't be a new fleet

        if you check a car before that, and it DOESN'T reach target before farther car, it's a new fleet

        tricky:
        - cars will get blocked by n+1 cars going slower, yes, BUT...
            - how can you tell if the car ahead would block you IF THAT car got blocked?
            - > maybe tag it somehow?
            - > oh, you need to know to track that original slowest car - that's the concerning one

        "if this care takes more time to target than the slowest car/fleet ahead of it, +=1 fleet"

        stack: have to worry about the next slowest car ahead
        no need to pop?
        len(stack) is the answer
        """

        zipped = list(zip(position, speed))
        zipped.sort(key=lambda i: i[0], reverse=True)

        stack = [] # Holds time-to-targets of cars farther along
        for pos, speed in zipped:
            timeToTarget = (target - pos) / speed
 
            if not stack or timeToTarget > stack[-1]:
                stack.append(timeToTarget)

        return len(stack)