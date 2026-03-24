# https://leetcode.com/problems/add-two-numbers

from ListNode import ListNode

class Solution(object):
    def list_length(self, node):
        l = 0
        while node != None:
            l += 1
            node = node.next
        return l

    def list_to_num(self, l):
        length = self.list_length(l)
        arr = []
        node = l
        while node != None:
            arr.append(node.val)
            node = node.next
        tot = 0
        i = 1
        while len(arr) > 0:
            num = arr.pop()
            tot += num * pow(10, length - i)
            i += 1
        return tot

    def num_to_list(self, num):
        if num < 10:
            return ListNode(num)
        rem = num
        stack = []
        while rem > 0:
            dig = rem % 10
            rem //= 10
            stack.append(dig)
        head = None
        while len(stack) > 0:
            dig = stack.pop()
            node = ListNode(dig)
            node.next = head
            head = node
        return head

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
       """
        num1 = self.list_to_num(l1)
        num2 = self.list_to_num(l2)
        tot = num1 + num2
        ltot = self.num_to_list(tot)
        return ltot

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [2,4,3],
            [5,6,4],
            [7,0,8],
        ),
        (
            [9,9,9,9,9,9,9],
            [9,9,9,9],
            [8,9,9,9,0,0,0,1],
        ),
        (
            [0],
            [0],
            [0],
        ),
        (
            [2,4,9],
            [5,6,4,9],
            [7,0,4,0,1],
        ),
    ]
    for (l1, l2, solution) in tests:
        print("------------------------")
        l1 = ListNode.from_array(l1)
        l2 = ListNode.from_array(l2)
        solution = ListNode.from_array(solution)
        result = sol.addTwoNumbers(l1, l2)
        print(f"l1={l1}, l2={l2}, solution={solution}, result={result}")
    # print("✅ All tests passed")

