# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return [True, 0]
            isleft, left = helper(root.left)
            isright, right = helper(root.right)
            return [isleft and isright and abs(left - right)<=1,max(left, right)+1]
        ans, _ = helper(root)
        return ans