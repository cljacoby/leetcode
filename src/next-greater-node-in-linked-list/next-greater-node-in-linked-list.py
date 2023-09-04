# https://leetcode.com/problems/next-greater-node-in-linked-list

from ListNode import ListNode

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        solution = []
        index = 0
        while head != None:
            solution.append(0)
            while len(stack) > 0 and head.val > stack[-1][1]:
                (i, _) = stack.pop()
                solution[i] = head.val
            stack.append((index, head.val))
            index += 1
            head = head.next
        return solution
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [2,1,5],
            [5,5,0],
        ),
        (
             [2,7,4,3,5],
             [7,0,5,5,0],
        )
    ]
    for (arr, solution) in tests:
        head = ListNode.from_array(arr)
        result = sol.nextLargerNodes(head)
        print(f"arr={arr}, result={result}")
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

