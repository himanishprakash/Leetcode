# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        self.diameter = 0

        def diameter(node):

            if not node:
                return 0

            left_node = diameter(node.left)
            right_node = diameter(node.right)
            self.diameter = max(self.diameter, left_node + right_node)
            return max(left_node, right_node) + 1

        diameter(root)

        return self.diameter