# https://leetcode.com/problems/clone-graph


'''
Key insights:
    1.) You need an intermediary data structure to place nodes into, and
    then assemble the linkages while you traverse the original
    hierarchy. You can't do this like the `same-tree` solution where you
    just walk to trees simultaneously.
'''

from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None
        hold = dict()
        seen = set()
        # self.clone_dfs(node, hold, seen)
        self.clone_bfs(node, hold, seen)
        nid = id(node)
        return hold[nid]

    def clone_dfs(self, node, hold, seen):
        nid = id(node)
        if nid in seen:
            return
        seen.add(nid)
        if nid not in hold:
            hold[nid] = Node(node.val)
        for nbor in node.neighbors:
            nborid = id(nbor)
            if nborid not in hold:
                hold[nborid] = Node(nbor.val)
            hold[nid].neighbors.append(hold[nborid])
            self.clone_dfs(nbor, hold, seen)

    def clone_bfs(self, node, hold, seen):
        que = deque([node])
        while len(que) > 0:
            node = que.popleft()
            nid = id(node)
            if nid in seen:
                continue
            seen.add(nid)
            if nid not in hold:
                hold[nid] = Node(node.val)
            for nbor in node.neighbors:
                nborid = id(nbor)
                if nborid not in hold:
                    hold[nborid] = Node(nbor.val)
                hold[nid].neighbors.append(hold[nborid])
                que.append(nbor)

if __name__ == "__main__":
    sol = Solution()
    
    n1 = Node(val=1)
    n2 = Node(val=2)
    n3 = Node(val=3)
    n4 = Node(val=4)
    n1.neighbors.append(n2)
    n2.neighbors.append(n3)
    n3.neighbors.append(n4)
    n4.neighbors.append(n1)

    clone = sol.cloneGraph(n1)
