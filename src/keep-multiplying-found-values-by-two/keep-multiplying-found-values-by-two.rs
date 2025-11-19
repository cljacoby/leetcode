// https://leetcode.com/problems/keep-multiplying-found-values-by-two
struct Solution;

use std::{collections::HashSet, iter::FromIterator};

impl Solution {
    pub fn find_final_value(nums: Vec<i32>, original: i32) -> i32 {
        let mut k = original;
        let set: HashSet<i32> = HashSet::from_iter(nums.into_iter());

        while set.contains(&k) {
            k = k * 2;
        }

        k
    }
}

fn main() {
    let tests = [
        (vec![5,3,6,1,12], 3, 24),
        (vec![2,7,9], 4, 4),
    ];


    for (nums, k, solution) in tests {
        let result = Solution::find_final_value(nums, k);
        assert_eq!(result, solution);
    }

}
