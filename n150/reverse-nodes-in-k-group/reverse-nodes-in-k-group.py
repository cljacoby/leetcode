# https://leetcode.com/problems/reverse-nodes-in-k-group

from ListNode import ListNode

class Solution(object):
    def link_nodes(self, bucket):
        head = tail = None
        for node in bucket:
            if head == None:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next
        return (head, tail)


    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        buckets = [[]]
        b = 0
        node = head
        while node != None:
            if len(buckets[b]) == k:
                buckets.append([])
                b += 1
            buckets[b].append(node)
            node = node.next
            buckets[b][-1].next = None
        print(f"finish bucketing. buckets={buckets}")

        for bucket in buckets:
            if len(bucket) == k:
                bucket.reverse()
        print(f"finish reversing. buckets={buckets}")

        segments = []
        for bucket in buckets:
            tup = self.link_nodes(bucket)
            segments.append(tup)
        print(f"finish segmenting. segments={segments}")

        head = tail = None
        for (seg_head, seg_tail) in segments:
            if head == None:
                head = seg_head
                tail = seg_tail
            else:
                tail.next = seg_head
                while tail.next != None:
                    tail = tail.next
        print(f"finish linking. head={head}, tail={tail}")
        return head


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [1,2,3,4,5],
            2,
            [2,1,4,3,5],
        ),
        (
            [1,2,3,4,5],
            3,
            [3,2,1,4,5],
        ),
    ]
    for (nums, k, solution) in tests:
        print("-----------------------------------")
        ll = ListNode.from_array(nums)
        solution = ListNode.from_array(solution)
        result = sol.reverseKGroup(ll, k)
        print(f"result = {result}")
        assert result.to_array() == solution.to_array(), \
                f"result {result} != solution {solution}"
    print("✅ All tests passed")

