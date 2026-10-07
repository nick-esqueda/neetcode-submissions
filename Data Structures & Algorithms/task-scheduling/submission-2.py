import heapq
from collections import defaultdict
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        like filling in the spaces between the repeated tasks

        n = num cycles AFTER finishing the one
        last one doesn't count (no need for spaces)

        do you only need to know the most frequent tasks?
        what about case where 2/3/... have same frequency?
        what if the others you try to interleave don't fit within N?


        "A": 5
        "B": 5
        "C": 5
        n = 2

        ["A","A","A","B","C"], n = 3 
  
        how many pauses does each need before procesing repeat?
        "A": 3  -> 3 * 3 = 9
        "B": 1  -> 1 * 3 = 3
        "C": 1  -> 1 * 3 = 3
        n = 3 

        if n=0, then the result is just the count of all tasks

        do simulation
        track wait time before can use an ele again
        plan:
        - pick any one of the most freq tasks, use it
        - set a counter for that task - num iterations to wait before can use again.
            - must decrement on each turn
            - array bucket counter - O(24) to decrement all
        """


        taskCounts = defaultdict(int)
        for task in tasks:
            taskCounts[task] += 1

        # Put counts with letter in heap
        taskCountsHeap = [] # (taskCount, task) - (4, "A")
        for task, count in taskCounts.items():
            taskCountsHeap.append((count, task))
        heapq.heapify_max(taskCountsHeap)

        tasksLeft = sum(taskCounts.values())
        quarantine = deque([])
        totalCycles = 0
        while tasksLeft:
            # Remove quarantined tasks with 0 wait left and add to heap
            while quarantine and quarantine[0][0] == totalCycles:
                waitDoneTime, taskCount, task = quarantine.popleft()
                heapq.heappush_max(taskCountsHeap, (taskCount, task))

            if taskCountsHeap:
                # "Use" the most frequent task
                taskCount, task = heapq.heappop_max(taskCountsHeap)

                # ONLY IF you used one this iter. might need to wait
                tasksLeft -= 1

                if taskCount > 1:
                    # Quarantine tasks from the heap that you just used for N wait time?
                    quarantine.append((totalCycles + n + 1, taskCount - 1, task))

            totalCycles += 1
 
        return totalCycles
