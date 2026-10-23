"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        To make a deep copy of it, must recurse through and copy each as you go
        But to make a copy of one, you must copy it's neighbors
        Recursive 
        Create the node first when you get to it, and store it
        That way, when you get to it's neighbors which looks back at it, use the copy you stored

        Create neighbors in order to create this one
        When neighbors are being created, they need to create the current one
        But, stop it, and use the copied node that was stored
        Now since neighbor was fully created, can add it to the neighbor list
        """
        if not node:
            return None

        copies = {}
        visited = set()
        def dfs(node):
            if node.val in copies:
                return copies[node.val]
            if node in visited:
                return

            visited.add(node)
            copyNode = Node(node.val)
            copies[node.val] = copyNode

            for nei in node.neighbors:
                neiCopy = dfs(nei)
                copyNode.neighbors.append(neiCopy)

            return copyNode
        
        return dfs(node)