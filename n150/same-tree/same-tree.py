# https://leetcode.com/problems/same-tree

from TreeNode import TreeNode

class Solution(object):
    def step(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        a = self.step(p.left, q.left)
        b = self.step(p.right, q.right)
        return a and b
        
    def isSameTree(self, p, q):
        return self.step(p, q)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [1,2,3],
            [1,2,3],
            True,
        ),
        (
            [1,2],
            [1,None,2],
            False,
        ),
        (
            [1,2,1],
            [1,1,2],
            False,
        ),
    ]
    for (p, q, solution) in tests:
        print("----------------------")
        p = TreeNode.from_array(p)
        print("p:")
        p.print_tree()
        q = TreeNode.from_array(q)
        print("q:")
        q.print_tree()
        result = sol.isSameTree(p, q)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

