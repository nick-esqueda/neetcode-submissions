# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Redefine LCA as something with numbers? b/c BST, binary search

        "is p in the L or R subtree? is q in L or R subtree?"
        if p and q are in a subtree, this is an ancestor. how to know if it's the lowest?
        when recursing back up, need to return the very first time you see

        i.e. The first node traveling up that has p/q in the left (or self) and q/p in the right (or self)

        use BST nature to help you determine which direction to go

        isn't it just the first node you come across that is within p <=> q??

        1
          2
            7
           4  8
          3 6

        """
        min = p.val if p.val < q.val else q.val
        max = p.val if p.val > q.val else q.val
 
        def dfs(node):
            if node is None:
                return

            if min <= node.val <= max:
                return node
            elif node.val < min:
                return dfs(node.right)
            elif node.val > max:
                return dfs(node.left)


        return dfs(root)