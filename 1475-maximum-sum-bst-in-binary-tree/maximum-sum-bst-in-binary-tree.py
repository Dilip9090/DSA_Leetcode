# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 0

        def dfs(node):
            if not node:
                return (True, float('inf'), float('-inf'), 0)

            left_bst, left_min, left_max, left_sum = dfs(node.left)
            right_bst, right_min, right_max, right_sum = dfs(node.right)

            if left_bst and right_bst and left_max < node.val < right_min:
                curr_sum = left_sum + right_sum + node.val
                self.ans = max(self.ans, curr_sum)

                return (
                    True,
                    min(left_min, node.val),
                    max(right_max, node.val),
                    curr_sum
                )

            return (False, float('-inf'), float('inf'), 0)

        dfs(root)
        return self.ans