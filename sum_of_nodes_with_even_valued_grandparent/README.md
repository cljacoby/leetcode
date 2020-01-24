## Problem
* **Problem Name**: sum_of_nodes_with_even_valued_grandparent
* **Link**: [sum_of_nodes_with_even_valued_grandparent](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/)
* **Difficulty**: Medium 
* **Finished**: :x: 
* **Tries to Complete**: 1,2,3, ...
* **Time to Complete**: 10 minutes, 20 minutes, 30 minutes, ...

## Problem Statement
Given a binary tree, return the sum of values of nodes with even-valued grandparent.
A grandparent of a node is the parent of its parent, if it exists.
If there are no nodes with an even-valued grandparent, return 0.

### Example 1:

**Input**:
```
root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
```

**Output**:
```
18
```
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.


## Notes:
* First attempted with recursive solution, passing references to parent and grandparent node; however,
* this doesn't account for grandparent nodes which were already summed. Hence, you wind up double counting nodes a lot.
* Nevermind, read the problem statement wrong, and it's easier than I thought.
  I was trying to sum the values of the grandparent nodes, rather than the node values whose grandparents were even
* Overall pretty easy, although I was really slow. Should've read the question more carefully
