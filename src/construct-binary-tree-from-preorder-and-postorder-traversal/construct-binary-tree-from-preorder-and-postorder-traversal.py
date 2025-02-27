# https://leetcode.com/problems/construct-binary-tree-from-pre-and-post-traversal

from TreeNode import TreeNode
from collections import deque

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(pre) == 0:
            return None
        pre = deque(pre)
        post = deque(post)
        val = pre.popleft()
        root = TreeNode(val)
        self.step(root, pre, post)
        return root

    def step(self, root, pre, post):
        # left
        if root.val == post[0]:
            post.popleft()
            return
        val = pre.popleft()
        node = TreeNode(val)
        root.left = node
        self.step(root.left, pre, post)
        
        # right
        if root.val == post[0]:
            post.popleft()
            return
        val = pre.popleft()
        node = TreeNode(val)
        root.right = node
        self.step(root.right, pre, post)

        assert root.val == post[0]
        post.popleft()

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [1,2,4,5,3,6,7],
            [4,5,2,6,7,3,1],
            [1,2,3,4,5,6,7],
        )
    ]
    for (pre, post, arr) in tests:
        tree = sol.constructFromPrePost(pre, post)
        solution = TreeNode.from_array(arr)
        print("tree:")
        tree.print_tree()
        print("tree:")
        solution.print_tree()

