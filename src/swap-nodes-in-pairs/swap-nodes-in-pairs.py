# https://leetcode.com/problems/swap-nodes-in-pairs

from ListNode import ListNode

class Solution(object):
    def swapPairs(self, head):
        stack = []
        node = head
        while node != None:
            a = node
            b = node.next
            stack.append((a, b))
            if node.next:
                node = node.next.next
            else:
                node = None
        tip = None
        while len(stack) > 0:
            (a, b) = stack.pop()
            if b:
                a.next = tip
                b.next = a
                tip = b
            else:
                tip = a
        return tip


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,2,3,4], [2,1,4,3]),
        ([1,2,3,4,5], [2,1,4,3,5]),
        ([1], [1]),
    ]
    for (nums, solution) in tests:
        sol = Solution()
        head = ListNode.from_array(nums)
        solution = ListNode.from_array(solution)
        head = sol.swapPairs(head)
        s1, s2 = str(head), str(solution)
        print(f"s1={s2}, s2={s2}")
        assert s1 == s2, \
            f"s1 {s1} != s2 {s2}"
    print("✅ All tests passed")

