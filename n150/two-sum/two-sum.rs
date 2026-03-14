// https://leetcode.com/problems/two-sum
struct Solution;

/** 
 * Summary:
 * - Build a HashMap of `nums`, where the key is the number, and the value
 *   is the index within `nums`.
 * - Iterate, over `nums`, and for each number calculate `diff` as the difference
 *   of `target` - `num`.
 * - Check if `diff` is in the map, which would indicate we have a match of two
 *   numbers which can sum to `target`
 * - Add a catch then when indexing in to the map, we don't re-use the same index
 *   twice.
 *
 *  Time Complexity: O(n)
 *  Space Complexity: O(n)
 * */

use std::{
    collections::{HashMap, HashSet},
    iter::FromIterator,
};

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let iter = nums
            .clone()
            .into_iter()
            .enumerate()
            .map(|(idx, val)| (val, idx));
        let map: HashMap<i32, usize> = HashMap::from_iter(iter);

        for (i, num) in nums.iter().enumerate() {
            let diff = target - num;
            if let Some(j) = map.get(&diff) {
                // edge-case: we cannot re-use the same index, i.e. if target is 6,
                // we cannot use a single index corresponding to a value of 3 twice.
                if *j == i {
                    continue;
                }
                return vec![i as i32, *j as i32];
            }
        }

        panic!("no solution in nums: {nums:?}");
    }
}

fn main() {
    let tests = vec![
        (vec![2, 7, 11, 15], 9, vec![0, 1]),
        (vec![3, 2, 4], 6, vec![1, 2]),
        (vec![3, 3], 6, vec![0, 1]),
    ];

    for (nums, target, solution) in tests {
        let result = Solution::two_sum(nums, target);
        let s_result: HashSet<i32> = HashSet::from_iter(result);
        let s_solution: HashSet<i32> = HashSet::from_iter(solution);
        // note: assumes there is one solution in nums
        assert_eq!(s_result, s_solution);
    }
}
