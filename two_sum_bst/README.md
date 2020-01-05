## Two Sum BST
* **Problem Name**: Two Sum BST
* **Link**: [Name](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)
* **Difficulty**: Easy
* **Finished**: :x:
* **Tries to Complete**: 1,2,3, ...
* **Time to Complete**: 10 minutes, 20 minutes, 30 minutes, ...

## Problem Statement
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

## Notes
* Use a dict to store values
* Key the element value to the index
* Recurse down tree and store all values
* Iterate over dict at end
*
