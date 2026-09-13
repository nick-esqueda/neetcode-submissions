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
        iterate through each node's adjList
        make sure to add to visited set so don't recurse forever

        on each node:
        - traverse down adjList till find a node with no neighbors (other than prev)
        - make Node() with current val
        - set adjList?
        - return self (since )


        for each node in the adjList, makeNode()?
        - recusive call, passing in the neighbor

        how do you clone the neighbor you just came from?
        use the node's vals instead of actual node? will that help?
        """

        if node is None:
            return None

        def clone(node, nodeMap):
            # If this node was already created, we're about to infinite loop, so...
            if node.val in nodeMap:
                # Return the node we already created
                # This will put the node in the adjList up the call stack
                return nodeMap[node.val] 

            adjList = []
            copyNode = Node(node.val, adjList)
            nodeMap[node.val] = copyNode

            for neighbor in node.neighbors:
                newNode = clone(neighbor, nodeMap)
                adjList.append(newNode)

            return copyNode
            
        return clone(node, dict())