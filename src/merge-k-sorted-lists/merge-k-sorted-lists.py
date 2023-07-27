# https://leetcode.com/problems/merge-k-sorted-lists

from ListNode import ListNode
from heapq import heappush, heappop

# Using built-in heap functionality makes this so easy it's basically
# cheating. Writing my own heapque implementation would be a good
# exercise.
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == [] or all(map(lambda x: x == None, lists)):
            return None
        heap = []
        for node in lists:
            while node != None:
                heappush(heap, node.val)
                node = node.next
        head = node = ListNode(heappop(heap))
        while len(heap) > 0:
            next_node = ListNode(heappop(heap))
            node.next = next_node
            node = node.next
        return head

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [[1, 4, 5], [1, 3, 4], [2, 6]],
            [1, 1, 2, 3, 4, 4, 5, 6],
        ),
    ]
    for (lists, solution) in tests:
        lists = [ListNode.from_array(l) for l in lists]
        result = sol.mergeKLists(lists).to_array()
        assert result == solution, f"result {result} != solution {solution}"
    print("✅ All tests passed")
