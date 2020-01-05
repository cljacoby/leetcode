## Two Sum
* **Problem Name**: Two Sum
* **Link**: [Two Sum](https://leetcode.com/problems/two-sum/)
* **Difficulty**: Easy
* **Tries to Complete**: 3
* **Time to Complete**: 25:56

## Problem Statement
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

## Notes

### Mistakes:
* I used slicing to reduce redundant iterations; however, I was also using python's `enumerate` for indexing. If you use `enumerate` on a slice, the indices are relative to the slice, so you need to use the kwarg `start`
* I also basically botched the slicing completely on the first try. If you do `array[0:]`, this will include the 0th element. On the first try I thought it would be first element after 0th.
* I almost mistakenly returned the elements rather than the indices. Read the problem carefully
* There is also a better solution using a hashset and a subtraction operation to lookup the right answer, rather then searching with iteration
