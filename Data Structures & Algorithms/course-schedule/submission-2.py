class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        one prereq = [a, b]
        means you MUST take b FIRST before a
        i.e., 'a' has a prereq of 'b'

        can you take courses simultaneously? does it matter?
        doesn't matter because just trying to see if possible/no cycles

        "does this course have a prereq?"
        if no, can take it first/start there


        {
            0: [1]
            1: []
        }


        {
            0: [4]
            1: [0]
            2: [0]
            3: [2]
            4: [1]
        }
        [[2, 0], [3, 2], [4, 1], [0, 4], [1, 0]]  
        0 -> 1 -> 2 -> 3 -> 4

        numCourses=5
        prerequisites=[[1,4],[2,4],[3,1],[3,2]]
        {
            0: []
            1: [4, ]
            2: [4, ]
            3: [1, 2]
            4: []
        }
        """
        
        adjList = { n: [] for n in range(numCourses) }
        
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        

        goodPaths = set()
        def dfs(node, visited):
            if node in visited:
                return False
            if node in goodPaths:
                return True
            
            visited.add(node)

            for child in adjList[node]:
                if not dfs(child, visited):
                    return False
            
            visited.remove(node)
            goodPaths.add(node)
            return True

        for course in adjList:
            if not dfs(course, set()):
                return False
        
        return True
