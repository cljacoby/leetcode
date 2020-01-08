from types import SimpleNamespace as Ns
import unittest as ut
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    @staticmethod
    def ll_to_list(head: ListNode):
        """Convert linked list values to list."""
        if head == None:
            raise Exception("head can not be None.")
        arr = []
        node = head
        while node != None:
            arr.append(node.val)
            node = node.next
        return arr

    @staticmethod
    def list_to_ll(arr: list):
        """Convert list to linked list."""
        if len(arr) == 0:
            raise Exception("list cannot be empty")
        head = ListNode(arr.pop(0))
        node = head
        while len(arr) != 0:
            next_node = ListNode(arr.pop(0))
            node.next = next_node
            node = next_node
        return head

    def calc_int(self, arr: list):
        """Interpret a list of 0s and 1s as a binary number, and calculate equivalent int."""
        return sum([pow(2, i) * el for i, el in enumerate(reversed(arr))])
    
    def getDecimalValue(self, head: ListNode) -> int:
        """Solution method."""
        arr = Solution.ll_to_list(head)
        num = self.calc_int(arr)
        return num


class TestSolution(ut.TestCase):
    def test_list_to_ll_negatives(self):
        """Test negative cases for method list_to_ll"""
        neg_tests = [Ns(input=[], output=None)]
        for case in neg_tests:
            try:
                Solution.list_to_ll(case.input)
            except:
                continue
            self.fail(f"Negative test case passed. Input = {case.input}")

    def test_list_to_ll_positives(self):
        """Test positive cases for method list_to_ll"""
        # head_1 = ListNode(1)
        # head_1.next = ListNode(2)
        # head_1.next.next = ListNode(3)
        # pos_tests = [Ns(input=[1, 2, 3], output=head_1)]
        # for case in pos_tests:
        #     index = 0
        #     node = Solution.list_to_ll(case.input)
        #     a_node = case.output
        #     while node != None:
        #         self.assertEqual(case.input[index], node.val)
        #         node = node.next
        #         index += 1
        #     self.assertEqual(index, len(case.input))

    # =========================================================================
    # =========================================================================

    def cases(self):
        """Main test cases."""
        return [
            Ns(input=Solution.list_to_ll([1, 0, 1]), output=5),
            Ns(input=Solution.list_to_ll([0]), output=0),
            Ns(input=Solution.list_to_ll([1]), output=1),
            Ns(
                input=Solution.list_to_ll(
                    [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
                ),
                output=18880,
            ),
            Ns(input=Solution.list_to_ll([0, 0]), output=0),
        ]

    def test_main(self):
        """Test Solution method."""
        method = "getDecimalValue"
        sol = Solution()
        for case in self.cases():
            result = getattr(sol, method)(case.input)
            self.assertEqual(result, case.output)


if __name__ == "__main__":
    ut.main()
