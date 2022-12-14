# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        nodes = 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        if left_height == right_height:
            nodes = 2 ** left_height + self.countNodes(root.right)
        else:
            nodes = 2 ** right_height + self.countNodes(root.left)
        return nodes
        
        
    def getHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height
      
# RUNTIME
# Runtime: 70 ms
# Performance: 99.25%

# MEMORY
# Memory: 21.4 MB
# Performance: 87.6%
