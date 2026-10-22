# https://leetcode.com/problems/clone-graph

'''
Notes:
    - Solved the problem by writing the conversion methods go from:
      - adjaceny list   ->      graph
      - graph           ->      adjaceny list
    - Probably not the fastest runtime, since I'm doing some extra work
      to first build the entire adjacency list, and then recreate a
      graph. You could in theory just go directly to creating a new
      graph as you traverse the original
    - But was kind of fun doing it this way, reminds me of CS6515 problems
      where graphs are frequently handled as adjacency lists rather than
      pointer based graphs
'''

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    
    def __repr__(self):
        s = f"Node {{ val: {self.val}, neighbors: {[n.val for n in self.neighbors]} }}"
        return s

    def __str__(self):
        return self.__repr__()

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        adj_list = self.graph_to_adj_list(node)
        graph = self.adj_list_to_graph(adj_list)
        return graph

    def adj_list_to_graph(self, adj_list):
        if len(adj_list) == 0:
            return None
        nodes = dict()
        for (i, edges) in enumerate(adj_list):
            val = i + 1
            node = Node(val)
            nodes[val] = node
        for (i, edges) in enumerate(adj_list):
            val = i + 1
            for neighbor in edges:
                nodes[val].neighbors.append(nodes[neighbor])
        # print(f"adj_list_to_graph. nodes: {nodes}")
        return nodes[1]
    
    def graph_to_adj_list(self, root):
        if root == None:
            return []
        nodes = dict()
        self._build(root, nodes)
        adj_list = []
        for i in range(1, len(nodes) + 1):
            adj_list.append(nodes[i].neighbors)
        # print(f"graph_to_adj_list. adj_list={adj_list}")
        return adj_list

    def _build(self, root, nodes):
        neighbors = [n.val for n in root.neighbors]
        node = Node(root.val, neighbors=neighbors)
        nodes[node.val] = node
        for neighbor in root.neighbors:
            if neighbor.val not in nodes:
                self._build(neighbor, nodes)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[2,4],[1,3],[2,4],[1,3]]),
        ([[]]),
        ([]),
    ]
    for (adj_list) in tests:
        print("------------------------------------------------")
        graph = sol.adj_list_to_graph(adj_list)
        result = sol.cloneGraph(graph)
        print(f"graph = {graph}")
        print(f"result = {result}")
        print(f"adj_list = {adj_list}")
        print(f"result (adj_list) = {sol.graph_to_adj_list(result)}")
    # print("✅ All tests passed")

