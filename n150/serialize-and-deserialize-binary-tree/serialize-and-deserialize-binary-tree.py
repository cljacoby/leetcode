# https://leetcode.com/problems/serialize-and-deserialize-binary-tree

from TreeNode import TreeNode
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        q = deque([root])
        buf = []
        while len(q) > 0:
            node = q.popleft()
            val = str(node.val) if node != None else "null"
            buf.append(val)
            if val == "null":
                continue
            q.append(node.left)
            q.append(node.right)
        # strip trailling nulls, which are not needed
        while len(buf) > 0 and buf[-1] == "null":
            buf.pop()
        s = ",".join(buf)
        return s

    def _deserialize(self, q):
        val = q.popleft()
        root = TreeNode(int(val))
        lvl_prev = deque([root])
        while len(q) > 0:
            lvl_next = deque([])
            while len(lvl_prev) > 0:
                parent = lvl_prev.popleft()
                # left
                if len(q) == 0:
                    return root
                val = q.popleft()
                if val != "null":
                    parent.left = TreeNode(int(val))
                    lvl_next.append(parent.left)
                # right
                if len(q) == 0:
                    return root
                val = q.popleft()
                if val != "null":
                    parent.right = TreeNode(int(val))
                    lvl_next.append(parent.right)
            lvl_prev = lvl_next
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        q = deque(data.split(","))
        if len(q) > 0 and q[0] == "null":
            return None
        root = self._deserialize(q)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

if __name__ == "__main__":
    codec = Codec()
    tests = [
        (
            [1,2,3,None,None,4,5],
        ),
    ]
    for (nums,) in tests:
        print("------------------------------------------")
        tree = TreeNode.from_array(nums)
        tree.print_tree()
        ser = codec.serialize(tree)
        print(f"serialized: {ser}")
        copy = codec.deserialize(ser)
        copy.print_tree()

