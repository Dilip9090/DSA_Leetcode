# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        ans = 0
        q = deque([(root, 0)])

        while q:
            size = len(q)
            _, first = q[0]
            last = first

            for _ in range(size):
                node, idx = q.popleft()
                idx -= first
                last = idx

                if node.left:
                    q.append((node.left, 2 * idx + 1))

                if node.right:
                    q.append((node.right, 2 * idx + 2))

            ans = max(ans, last + 1)

        return ans