class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        sorted ascending by start
        input is non-overlapping
        []

        put newInterval inside intervals, in sorted order
        merge them if you need

            [2,5]
        [[1,3][4,6]]
            [2,7]
        [[1,3][4,6]]
            [2,6]
        [[1,3][4,7]]

        if the start intersects prev interval, merge up till max(interval[1], newInterval[1])
        if the end intersects next interval, merge starting on min(interval[1], newInterval[1])

        but what if interval is fully inside another?

        compare newInterval with insertion point - 1 (i - 1)
        if start is within the bounds of prev interval...
        - start creating a combined interval:
            - set combined start to the min of the two starts
            - set combined end to the max of the two starts
        could insert now, BUT, might be overlapping with i + 1!

        compare combined (or newInterval if not combined) with i + 1
        if end is within the bounds of next interval...
        - start creating (or reuse??) a combined interval:
            - will i + 1's start always be erased here??
            - set combined end to the max of the two ends
        
        how to replace?


               [6,7]
        [[1,2],[3,5],[9,10]]

        CASES:
        - is perfectly between two of them
        - is perfectly within one
        - starts within one and ends before next start
        - starts within one and ends within next
        - starts within one and ends after next end
        - starts between two and ends within next
        - starts between two and ends after next end
        - is fully before 0
        - is fully after last
        - starts before 0 but ends within first
        - starts before 0 and ends after first
        - starts within last but ends after last


        [[1,2],[3,5],[9,10]], newInterval = [6,7] / [6,12] / [4, 11]
                     [6,7]
        [[1,2],[3,5]         ] 

        result = []
        i = 0
        while newInter[0] > intervals[i][1]:
            result.add(intervals[i])
            i += 1
        
        # At this point, i is within or before next

        # Choose start num
        combined = [0, 0]
        combined[0] = min(intervals[i][0], newInter[0]) # smaller of new inter vs. ith inter

        # Find end num
        # If newEnd spans until several inters, need to loop to find it (or if hit end)
        # What comparison do you need for that though?
        while i < len(intervals) and newEnd > currInter[1]:
            i += 1 # Need to find the inter that beats newInter
        
        # At this point, i is either:
        # - At the end of the list (i == n)
        # - On the inter who's end is bigger than newInter
        # So, set the end 

        combined[1] = newInter[1] if i == len(intervals) else intervals[i][1]
        result.append(combined)

        # But need to know whether to keep iterating or not! Or handled automatically by i??

        while i < len(intervals): # will skip automatically if at end
            result.append(intervals[i])
            i += 1
 
        return result
        """

        result = []
        i = 0

        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
            i += 1
        
        combined = [newInterval[0], newInterval[1]]
        if i < len(intervals):
            combined[0] = min(intervals[i][0], newInterval[0])

        while i < len(intervals) and newInterval[1] > intervals[i][1]:
            i += 1

        if i >= len(intervals) or newInterval[1] < intervals[i][0]:
            combined[1] = newInterval[1]
        else:
            combined[1] = intervals[i][1]
            i += 1
 
        result.append(combined)

        while i < len(intervals):
            result.append(intervals[i])
            i += 1
 
        return result